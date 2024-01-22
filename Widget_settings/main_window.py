import cv2
import numpy as np
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QMessageBox, QGraphicsLineItem, QDialog
from PyQt5.QtCore import Qt, pyqtSlot as Slot, pyqtSignal as Signal, QTimer
from Enums.State_scenario import State_scenario
from UI.UI_window import Ui_MainWindow
from Widget_settings.Joystick import Joystick
from UI.target_or_human import Ui_Dialog
from Enums.Videso_Size import Video_Size as VIDEO_SIZE
class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

class Main_Window(QMainWindow):

    signal_send_packages_to_server = Signal(int)
    signal_close_event = Signal()
    signal_send_position_click = Signal(int, int)
    signal_send_sonar = Signal(int)

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.init_ui()
        self.connections()
        self.init_combo_box_item()



    def init_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dialog = MyDialog()
        self.ui.btn_settings.view().setMinimumWidth(690)
        self.ui.btn_settings.view().setSpacing(10)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_camera)
        self.ui.stackedWidget_btn.setCurrentWidget(self.ui.page_eyes)
        self.ui.btn_camera.setDisabled(True)
        self.ui.btn_map.setDisabled(False)
        self.ui.stackedWidget_turn.setCurrentIndex(2)
        self.ui.btn_sonar.setChecked(True)

        self.scale = 20

        self.timer_left = QTimer(self)
        self.timer_right = QTimer(self)
        self.timer_interval = 15

        self.palette = QPalette()

        self.joystick = Joystick()
        self.widget = self.ui.widget_joystick
        layout = QGridLayout()
        layout.addWidget(self.joystick)
        self.widget.setLayout(layout)

        self.Paint = self.ui.graphicsView


    def connections(self):
        self.ui.btn_camera.clicked.connect(self.show_page)
        self.ui.btn_map.clicked.connect(self.show_page)

        self.ui.btn_eyes.toggled.connect(self.handleButtonToggle)
        self.ui.btn_circle.toggled.connect(self.handleButtonToggle)
        self.ui.btn_infin.toggled.connect(self.handleButtonToggle)

        self.ui.btn_eyes.clicked.connect(self.show_human_or_target)


        self.ui.btn_circle.clicked.connect(self.slot_scenario_circle)
        self.ui.btn_infin.clicked.connect(self.slot_scenario_infinity)
        self.ui.btn_camera.clicked.connect(self.slot_scenario_control_surface)

        self.ui.btn_trajectory.toggled.connect(self.check_trajectory)

        self.ui.btn_remove_scale.clicked.connect(self.scale_map_remove)
        self.ui.btn_plus_scale.clicked.connect(self.scale_map_plus)

        self.ui.btn_left.pressed.connect(self.startTimer_left)
        self.ui.btn_left.released.connect(self.stopTimer_left)
        self.timer_left.timeout.connect(self.Paint.turn_left_platform)

        self.ui.btn_right.pressed.connect(self.startTimer_right)
        self.ui.btn_right.released.connect(self.stopTimer_right)
        self.timer_right.timeout.connect(self.Paint.turn_right_platform)

        self.ui.btn_plus.clicked.connect(self.Paint.plus_platform)
        self.ui.btn_remove.clicked.connect(self.Paint.remove_platform)

        self.dialog.ui.btn_human.clicked.connect(self.btn_human_clicked)
        self.dialog.ui.btn_target.clicked.connect(self.btn_target_clicked)

        self.dialog.ui.btn_human.clicked.connect(self.slot_scenario_following)
        self.dialog.ui.btn_target.clicked.connect(self.slot_scenario_following_target)

        self.ui.btn_sonar.clicked.connect(self.sonar_btn)


    def show_page(self):
        if self.ui.btn_camera.isChecked():
            self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_camera)
            self.ui.stackedWidget_btn.setCurrentWidget(self.ui.page_eyes)
            self.ui.btn_camera.setDisabled(True)
            self.ui.btn_map.setDisabled(False)
            self.ui.btn_trajectory.setChecked(False)
        if self.ui.btn_map.isChecked():
            self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_map)
            self.ui.stackedWidget_btn.setCurrentWidget(self.ui.page_settings)
            self.ui.btn_camera.setDisabled(False)
            self.ui.btn_map.setDisabled(True)
            #Отключение сценариев
            self.ui.btn_eyes.setChecked(False)
            self.ui.btn_infin.setChecked(False)
            self.ui.btn_circle.setChecked(False)
            self.dialog.ui.btn_human.setChecked(False)
            self.dialog.ui.btn_target.setChecked(False)
            style = self.setIcon_style(name='eyes')
            self.ui.btn_eyes.setStyleSheet(style)

    @Slot()
    def disconnect_scenarios(self):
        print('Дисконекст сценариев')
        self.ui.btn_eyes.setChecked(False)
        self.dialog.ui.btn_target.setChecked(False)
        self.dialog.ui.btn_human.setChecked(False)

        self.ui.btn_circle.setChecked(False)
        self.ui.btn_infin.setChecked(False)
        self.ui.btn_trajectory.setChecked(False)

    def show_hint(self, text):
        dialog = QMessageBox(self)
        dialog.setStyleSheet('QLabel{font: 40px;}\
                             QPushButton{width: 110px; height: 50px; font: 40px;\
                             border: 2px solid; \
                             border-radius: 6px;}}\
                             QMessageBox{width: 600px; height: 800px; \
                             border: 2px solid rgba(62, 63, 70, 0);\
                             border-radius: 10px;}')
        dialog.setText(text)
        dialog.setWindowFlags(Qt.FramelessWindowHint)
        dialog.move(self.Paint.scene.width()/2, self.Paint.scene.height()/2)
        dialog.setIcon(QMessageBox.Information)
        dialog.exec_()
        self.ui.btn_trajectory.setChecked(False)

    def startTimer_left(self):
        if not self.timer_left.isActive():
            self.timer_left.start(self.timer_interval)

    def startTimer_right(self):
        if not self.timer_right.isActive():
            self.timer_right.start(self.timer_interval)

    def stopTimer_left(self):
        if self.timer_left.isActive():
            self.timer_left.stop()

    def stopTimer_right(self):
        if self.timer_right.isActive():
            self.timer_right.stop()

    def show_human_or_target(self):
        self.ui.btn_eyes.setChecked(True)
        self.dialog.exec()
        if self.dialog.ui.btn_human.isChecked() or self.dialog.ui.btn_target.isChecked():
            self.ui.btn_eyes.setChecked(True)
        else:
            self.ui.btn_eyes.setChecked(False)
            style = self.setIcon_style(name='eyes')
            self.ui.btn_eyes.setStyleSheet(style)


    def btn_human_clicked(self):
        if self.dialog.ui.btn_human.isChecked():
            style = self.setIcon_style(name='emoji')
            self.ui.btn_eyes.setStyleSheet(style)
            self.dialog.ui.btn_target.setChecked(False)
            self.ui.btn_eyes.setChecked(True)
        else:
            self.ui.btn_eyes.setChecked(False)
            style = self.setIcon_style(name='eyes')
            self.ui.btn_eyes.setStyleSheet(style)
        self.dialog.close()

    def btn_target_clicked(self):
        if self.dialog.ui.btn_target.isChecked():
            self.dialog.ui.btn_human.setChecked(False)
            style = self.setIcon_style(name='target')
            self.ui.btn_eyes.setStyleSheet(style)
            self.ui.btn_eyes.setChecked(True)
        else:
            self.ui.btn_eyes.setChecked(False)
            style = self.setIcon_style(name='eyes')
            self.ui.btn_eyes.setStyleSheet(style)
        self.dialog.close()



    def scale_map_remove(self):
        if self.scale < 10:
            return
        else:
            self.scale -= 5
            items_to_remove = [item for item in self.Paint.scene.items() if item.zValue() == 2]
            for item in items_to_remove:
                self.Paint.scene.removeItem(item)
            self.Paint.scale_grid(scale=self.scale, width=int(self.Paint.scene.width()), height=int(self.Paint.scene.height()))
            self.scale_text_to_lab()

    def scale_text_to_lab(self):
        left = self.scale/5
        right = 4
        if left % 2 == 0:
            left = left / 2
            right = right / 2
            if left / 2 == 1:
                self.ui.label.setText(f'M {1}:{1}')
            else:
                self.ui.label.setText(f'M {int(left)}:{int(right)}')
        else:
            self.ui.label.setText(f'M {int(left)}:{int(right)}')

    def scale_map_plus(self):
        if self.scale > 30:
            return
        else:
            items_to_remove = [item for item in self.Paint.scene.items() if item.zValue() == 2]
            for item in items_to_remove:
                self.Paint.scene.removeItem(item)
            self.scale += 5
            self.Paint.scale_grid(scale=self.scale, width=int(self.Paint.scene.width()), height=int(self.Paint.scene.height()))
            self.scale_text_to_lab()

    def init_combo_box_item(self):
        self.ui.btn_settings.activated.connect(self.onComboBoxChanged)

    def onComboBoxChanged(self):
        self.ui.stackedWidget_size.setCurrentIndex(0)
        self.ui.stackedWidget_turn.setCurrentIndex(2)
        selected_option = self.ui.btn_settings.currentIndex()
        if selected_option == 0:
            self.Paint.loadSaveMap()
        elif selected_option == 1:
            self.Paint.save()
        elif selected_option == 2:
            self.Paint.clear()
        elif selected_option == 3:
            self.ui.stackedWidget_size.setCurrentIndex(1)
            self.ui.stackedWidget_turn.setCurrentIndex(1)
            self.Paint.addPlatform()
        elif selected_option == 4:
            self.Paint.addObstacle()
        elif selected_option == 5:
            self.Paint.paintTrajectory()
        elif selected_option == 6:
            self.ui.stackedWidget_size.setCurrentIndex(2)
            self.ui.stackedWidget_turn.setCurrentIndex(2)
            self.Paint.drawing = False
            self.Paint.drawing_rectangle = False


    def handleButtonToggle(self, checked):
        sender = self.sender()
        if checked:
            for button in [self.ui.btn_eyes, self.ui.btn_infin, self.ui.btn_circle]:
                if button is not sender:
                    button.setChecked(False)
                    self.ui.stackedWidget.setCurrentIndex(1)
            if self.ui.btn_circle.isChecked() or self.ui.btn_infin.isChecked():
                style = self.setIcon_style(name='eyes')
                self.ui.btn_eyes.setStyleSheet(style)
        else:
            self.ui.stackedWidget.setCurrentIndex(0)

    def setIcon_style(self, name):
        style = 'QPushButton {border:' \
                '2px solid rgba(62, 63, 70, 0);\
                border-radius: 6px;\
                background-color: rgba(62, 63, 70, 0.7);\
                image: url(UI/icons/'+str(name)+'.svg);\
                min-width: 80px;}\
                QPushButton:checked {\
                border: 2px solid rgba(217, 217, 217, 0);\
                border-radius: 6px;\
                background-color: rgba(217, 217, 217, 0.7);\
                min-width: 80px;}'
        return style


    @Slot(list)
    def paint_rectangle(self, coord_rect=None, image=None):
        if coord_rect != None:
            print('coord: ', coord_rect)
            image = cv2.rectangle(image, (coord_rect[0], coord_rect[1]), (coord_rect[2], coord_rect[3]), color=(0, 0, 255), thickness=2)
            return image
        else:
            return image

    @Slot(np.ndarray)
    def back_image(self, frame):
        image_np = frame
        #todo согласовать боксы и изображения
        # if self.ui.btn_eyes.isChecked():
        #     image_np = self.paint_rectangle(image=image_np)

        if image_np is not None:
            image_qt = QPixmap.fromImage(
                QImage(image_np.data, image_np.shape[1], image_np.shape[0], image_np.shape[1] * 3,
                       QImage.Format_RGB888))

            image_qt = image_qt.scaled(self.rect().width(), self.rect().height())

            brush = QBrush(image_qt)
            self.palette.setBrush(QPalette.Window, brush)
            self.ui.frame.setPalette(self.palette)
            self.ui.frame.setAutoFillBackground(True)

    def check_trajectory(self):
        if self.ui.btn_trajectory.isChecked():
            if self.Paint.Platform == None:
                self.show_hint(text='Добавьте платформу!')
                return
            if not any(isinstance(item, QGraphicsLineItem) and item.pen().color() == Qt.red for item in self.Paint.scene.items()):
                self.show_hint(text='Добавьте траекторию!')
                return

            self.Paint.move_platform()
            self.signal_send_packages_to_server.emit(State_scenario.TRAJECTORY.value)

    @Slot()
    def slot_scenario_following(self):
        if (self.dialog.ui.btn_human.isChecked() == False):
            return
        self.signal_send_packages_to_server.emit(State_scenario.FOLLOWING_HUMAN.value)
        print('following')

    @Slot()
    def slot_scenario_following_target(self):
        if (self.dialog.ui.btn_target.isChecked() == False):
            return
        self.signal_send_packages_to_server.emit(State_scenario.FOLLOWING_TARGET.value)
        print('following target')

    @Slot()
    def slot_scenario_infinity(self):
        if self.ui.btn_infin.isChecked() == False:
            return
        self.dialog.ui.btn_human.setChecked(False)
        self.dialog.ui.btn_target.setChecked(False)
        self.signal_send_packages_to_server.emit(State_scenario.INFINITY.value)
        print('infinity')

    @Slot()
    def slot_scenario_circle(self):
        if self.ui.btn_circle.isChecked() == False:
            return
        self.dialog.ui.btn_human.setChecked(False)
        self.dialog.ui.btn_target.setChecked(False)
        self.signal_send_packages_to_server.emit(State_scenario.CIRCLE.value)
        print('circle')

    @Slot()
    def slot_scenario_trajectory(self):
        if self.ui.btn_trajectory.isChecked() == False:
            return
        self.signal_send_packages_to_server.emit(State_scenario.TRAJECTORY.value)
        print('trajectory')

    @Slot()
    def slot_scenario_control_surface(self):
        if self.ui.btn_camera.isChecked() == False:
            return
        self.signal_send_packages_to_server.emit(State_scenario.CONTROL_BY_SURFACE.value)
        print('control_surface')


    def sonar_btn(self):
        if self.ui.btn_sonar.isChecked():
            self.signal_send_sonar.emit(0)
        else:
            self.signal_send_sonar.emit(1)

    def mousePressEvent(self, event):
        if self.dialog.ui.btn_human.isChecked():
            pos = self.calculate_current_position(event.pos())
            self.signal_send_position_click.emit(pos[0], pos[1])
        QMainWindow.mousePressEvent(self, event)

    def calculate_current_position(self, pos):
        x_ = int(VIDEO_SIZE.X.value / self.width() * pos.x())
        y_ = int(VIDEO_SIZE.Y.value / self.height() * pos.y())
        return x_, y_
