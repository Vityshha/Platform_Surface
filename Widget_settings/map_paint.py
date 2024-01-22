from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsLineItem, QFileDialog, QGraphicsPixmapItem, \
    QGraphicsRectItem
from PyQt5.QtCore import QLineF, QPoint
from PyQt5.QtGui import QPen, QPixmap, QPainter
from PyQt5 import QtGui

from Widget_settings.Platform import Platform
from PyQt5.QtCore import Qt
from Enums.State_scenario import State_scenario
from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot

import numpy as np
MAX_ANGLE = 35
MAX_DIST = 60 #cm

class Paint(QGraphicsView):

    signal_send_trajectory = Signal(str)
    signal_send_traj_start = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.drawing = False
        self.drawing_rectangle = False
        self.start_point = None
        self.end_point = None
        self.begin, self.destination = QPoint(), QPoint()
        self.pix = QPixmap(self.rect().size())
        self.pix.fill(Qt.white)
        self.Platform = None
        self.init_traj_const()

    def init_traj_const(self):
        self.trajectory = []
        self.rotate_angle = 0
        self.scale_factor = 1
        self.const_width = 318
        self.const_height = 140
        self.counter_angle = 0
        self.angle_rotate = self.rotate_angle
        self.count_dist = 0
        self.full_list_angle = []
        self.x_pos_list = []
        self.y_pos_list = []
        self.flag_start = True
        self.flag_start_turn = True
        self.index_dist = 0
        self.flag_start_turn_replay = False
        self.flag_end_move = False
        self.counter_null = 0


    def resizeEvent(self, event, scale=20):
        QGraphicsView.resizeEvent(self, event)
        self.scene.setSceneRect(0, 0, self.width(), self.height())
        self.scale_grid(scale=scale, width=int(self.scene.width()), height=int(self.scene.height()))


    def mousePressEvent(self, event):
        if self.drawing_rectangle:
            if event.buttons() & Qt.LeftButton:
                self.start_point = self.mapToScene(event.pos())
                self.current_rect = QGraphicsRectItem(self.start_point.x(), self.start_point.y(), 0, 0)
                self.current_rect.setPen(self.pen)
                self.current_rect.setZValue(4)
                self.scene.addItem(self.current_rect)
        else:
            if event.button() == Qt.LeftButton:
                self.start_point = event.pos()
                self.end_point = event.pos()
        QGraphicsView.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        if self.drawing_rectangle:
            if event.buttons() & Qt.LeftButton:
                self.end_point = self.mapToScene(event.pos())
                x = min(self.start_point.x(), self.end_point.x())
                y = min(self.start_point.y(), self.end_point.y())
                width = abs(self.start_point.x() - self.end_point.x())
                height = abs(self.start_point.y() - self.end_point.y())
                self.current_rect.setZValue(4)
                self.current_rect.setRect(x, y, width, height)
        else:
            if event.buttons() == Qt.LeftButton:
                self.start_point = self.end_point
                self.end_point = event.pos()
                if self.drawing:
                    self.draw_line()
        QGraphicsView.mouseMoveEvent(self, event)


    def mouseReleaseEvent(self, event):
        if self.drawing_rectangle:
            if event.button() & Qt.LeftButton:
                self.current_rect = None
                self.update()
        else:
            if event.button() == Qt.LeftButton:
                self.end_point = event.pos()
                if self.drawing:
                    self.draw_line()
                    self.start_point = None
                    self.end_point = None
        QGraphicsView.mouseReleaseEvent(self, event)

    def addObstacle(self):
        self.pen = QPen(Qt.black, 10)
        self.drawing = False
        self.drawing_rectangle = True
        if self.Platform != None:
            self.Platform.flag = False

    def paintTrajectory(self):
        self.pen = QPen(Qt.red, 10)
        self.drawing = True
        self.drawing_rectangle = False
        if self.Platform != None:
            self.Platform.flag = False


    def clear(self):
        items_to_remove = [item for item in self.scene.items() if item.zValue() != 2]
        for item in items_to_remove:
            self.scene.removeItem(item)
        self.Platform = None
        self.update()

        self.init_traj_const()

    def addPlatform(self):
        self.drawing = False
        self.drawing_rectangle = False
        self.setRenderHint(QtGui.QPainter.Antialiasing, False)
        self.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, False)
        if self.Platform == None:
            self.Platform = Platform(0, 0, 318, 140)
            self.Platform.setZValue(5)
            self.scene.addItem(self.Platform)
            self.Platform.flag = True
        elif self.Platform != None:
            self.Platform.flag = True


    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Сохранить как изображение", "", "JPEG(*.jpg);;All Files(*.*)")
        if filePath == "":
            return

        pixmap = QPixmap(self.scene.sceneRect().size().toSize())
        pixmap.fill(Qt.white)
        painter = QPainter(pixmap)
        self.scene.render(painter)
        painter.end()
        pixmap.save(filePath, "JPG")
        if self.Platform != None:
            self.Platform.flag = False

    def loadSaveMap(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Images (*.png *.xpm *.jpg)")
        if file_path:
            pixmap = QPixmap(file_path)
            pixmap_item = QGraphicsPixmapItem()
            pixmap_item.setPixmap(pixmap.scaled(self.rect().width(), self.rect().height()))
            pixmap_item.setZValue(1)
            self.scene.addItem(pixmap_item)
        if self.Platform != None:
            self.Platform.flag = False


    def draw_line(self):
        if self.start_point and self.end_point:
            line = QGraphicsLineItem(QLineF(self.mapToScene(self.start_point), self.mapToScene(self.end_point)))
            line.setPen(self.pen)
            line.setZValue(3)
            self.scene.addItem(line)
            self.trajectory.append([line.line().p1().x(), line.line().p1().y(), line.line().p2().x(), line.line().p2().y()])
        if self.drawing_rectangle:
            line = QGraphicsLineItem(self.start_point.x(), self.start_point.y(),
                                     self.end_point.x(), self.end_point.y())
            line.setPen(self.pen)
            line.setZValue(4)
            self.scene.addItem(line)

    def turn_left_platform(self):
        self.rotate_angle -= 1
        self.Platform.setRotation(self.rotate_angle)
        self.angle_rotate = self.rotate_angle

    def turn_right_platform(self):
        self.rotate_angle += 1
        self.Platform.setRotation(self.rotate_angle)
        self.angle_rotate = self.rotate_angle

    def plus_platform(self):
        if self.Platform.sceneBoundingRect().height() >= self.scene.sceneRect().height()-150 or self.Platform.sceneBoundingRect().width() >= self.scene.sceneRect().width()-150:
            return
        else:
            self.scale_factor += 0.1
            self.Platform.setScale(self.scale_factor)

    def remove_platform(self):
        if self.scale_factor < 0.5:
            return
        else:
            self.scale_factor -= 0.1
            self.Platform.setScale(self.scale_factor)


    def move_platform(self):
        self.signal_send_traj_start.emit(State_scenario.TRAJECTORY.value)
        x_plarform_start = self.Platform.pos().x() + (self.const_width/2) * np.cos(np.deg2rad(-self.rotate_angle))
        y_platform_start = self.Platform.pos().y() + 70 - (self.const_width/2) * np.sin(np.deg2rad(-self.rotate_angle))

        x_plarform_end = x_plarform_start + self.const_width * np.cos(np.deg2rad(-self.rotate_angle))
        y_platform_end = y_platform_start - self.const_width * np.sin(np.deg2rad(-self.rotate_angle))

        x_trajectory = [x2 for x1, y1, x2, y2 in self.trajectory]
        y_trajectory = [y2 for x1, y1, x2, y2 in self.trajectory]

        self.x0 = self.Platform.pos().x()
        self.y0 = self.Platform.pos().y() + 70


        x_trajectory, y_trajectory = self.clear_trajectory(x_trajectory, y_trajectory)
        self.x_pos_list = x_trajectory.copy()
        self.y_pos_list = y_trajectory.copy()

        x_trajectory.insert(0, x_plarform_start)
        y_trajectory.insert(0, y_platform_start)
        x_trajectory.insert(0, x_plarform_end)
        y_trajectory.insert(0, y_platform_end)

        data = self.angle_and_dist_package(x_trajectory, y_trajectory)

        #todo заглушка чтобы в конце лишних поворотов не было
        for _ in range(2):
            if data[-1] == 0:
                data = data[:-2]
            if data[-1] < 10:
                data = data[:-2]

        #todo чтобы лишнюю свою половину длины не проезжал
        self.len_platform = 140/2
        while self.len_platform > 0:
            if data[-1] > self.len_platform:
                # data[-1] = int(data[-1] - self.len_platform)
                data[-1] = int(data[-1])
                self.len_platform = 0
            else:
                self.len_platform -= data[-1]
                data = data[:-2]

        data = str(data)
        data = data[1:-1]
        self.signal_send_trajectory.emit(data)


    def clear_trajectory(self, x_trajectory, y_trajectory):
        i = 0
        while i < (len(x_trajectory) - 2):
            dx1 = (x_trajectory[i + 1] - x_trajectory[i]) / self.grid_size * 100
            dx2 = (x_trajectory[i + 2] - x_trajectory[i + 1]) / self.grid_size * 100
            dy1 = (y_trajectory[i + 1] - y_trajectory[i]) / self.grid_size * 100
            dy2 = (y_trajectory[i + 2] - y_trajectory[i + 1]) / self.grid_size * 100

            angle = np.degrees(np.arctan2(dy2, dx2) - np.arctan2(dy1, dx1))
            if abs(angle) < MAX_ANGLE or abs(angle) > 360-MAX_ANGLE:
                x_trajectory.pop(i + 1)
                y_trajectory.pop(i + 1)
            else:
                i += 1

        i = 0
        while i < (len(x_trajectory) - 2):
            dx1 = (x_trajectory[i + 1] - x_trajectory[i]) / self.grid_size * 100
            dy1 = (y_trajectory[i + 1] - y_trajectory[i]) / self.grid_size * 100

            dist = (dx1 ** 2 + dy1 ** 2) ** (1 / 2)
            if dist < MAX_DIST:
                x_trajectory.pop(i + 1)
                y_trajectory.pop(i + 1)
            else:
                i += 1
        return x_trajectory, y_trajectory

    def angle_and_dist_package(self, x_trajectory, y_trajectory):
        data = [1]
        self.list_dict_pack = []
        for i in range(len(x_trajectory)-2):
            dx1 = (x_trajectory[i + 1] - x_trajectory[i]) / self.grid_size * 100
            dx2 = (x_trajectory[i + 2] - x_trajectory[i + 1]) / self.grid_size * 100
            dy1 = (y_trajectory[i + 1] - y_trajectory[i]) / self.grid_size * 100
            dy2 = (y_trajectory[i + 2] - y_trajectory[i + 1]) / self.grid_size * 100

            angle = int(np.degrees(np.arctan2(dy2, dx2) - np.arctan2(dy1, dx1)))
            dist = int((dx2 ** 2 + dy2 ** 2) ** (1 / 2))

            if angle < -180:
                angle = 360 + angle
            elif angle > 180:
                angle = angle - 360

            if angle > 120:
                self.full_list_angle.append(angle)
                data.append(120)
                data.append(0)
                data.append(angle - 120)
                data.append(dist)
                self.list_dict_pack.append(dist)
            elif angle < -120:
                self.full_list_angle.append(angle)
                data.append(-120)
                data.append(0)
                data.append(angle+120)
                data.append(dist)
                self.list_dict_pack.append(dist)
            else:
                self.full_list_angle.append(angle)
                data.append(angle)
                data.append(dist)
                self.list_dict_pack.append(dist)
        return data


    def scale_grid(self, scale, width, height):
        self.grid_size = 10 * scale

        for x in range(0, width, self.grid_size):
            line = QGraphicsLineItem(x, 0, x, height)
            line.setZValue(2)
            self.scene.addItem(line)

        for y in range(0, height, self.grid_size):
            line = QGraphicsLineItem(0, y, width, y)
            line.setZValue(2)
            self.scene.addItem(line)


    @Slot(list)
    def setPosPlatform(self, data=None):

        dist = data

        if len(self.x_pos_list) == 0:
            return
        elif dist[2] == 0 and dist[1] == 0:
            return

        self.full_dist = 0
        #пока не придет нужная команда и пока не закончит разворот
        if dist[1] == 0 and self.flag_start:
            self.flag_end_move = True
            self.counter_null += 1
            self.full_dist += dist[2]
            dx1 = (self.x_pos_list[self.count_dist] - self.x0)
            dy1 = (self.y_pos_list[self.count_dist] - self.y0)
            dist_new = round(int((dx1 ** 2 + dy1 ** 2) ** (1 / 2)) / self.grid_size * 100, 3)

            if self.list_dict_pack[self.index_dist] <= 0:
                return
            else:
                self.list_dict_pack[self.index_dist] = self.list_dict_pack[self.index_dist] - dist[2]

            if dist_new == 0:
                return

            ksi = self.full_dist / dist_new
            x_new = self.x0 + ksi * dx1
            y_new = self.y0 + ksi * dy1 - 70

            if self.list_dict_pack[self.index_dist] <= 0:
                self.Platform.setPos(self.x_pos_list[self.count_dist], self.y_pos_list[self.count_dist] - 70)
                self.x0 = x_new
                self.y0 = y_new + 70
            else:
                self.Platform.setPos(x_new, y_new)
                self.x0 = x_new
                self.y0 = y_new + 70

        # #начало поворота
        elif dist[1] == 1:
            self.flag_start = False
            self.flag_start_turn_replay = True
            self.full_dist = 0
            if len(self.full_list_angle) <= self.counter_angle:
                return
            self.angle_rotate += self.full_list_angle[self.counter_angle]

        #конец поворота
        elif dist[1] == 2:
            if self.counter_null > 3 and self.flag_end_move:
                self.count_dist += 1
                self.index_dist += 1
                self.flag_end_move = False
                self.flag_start = False
            else:
                self.flag_end_move = True
                self.flag_start = True
                if self.flag_start_turn_replay:
                    self.flag_start_turn_replay = False

                    self.full_dist = 0
                    self.Platform.setRotation(self.angle_rotate)
                    self.counter_angle += 1

                else:
                    if len(self.full_list_angle) <= self.counter_angle:
                        return
                    self.angle_rotate += self.full_list_angle[self.counter_angle]
                    self.Platform.setRotation(self.angle_rotate)
                    self.counter_angle += 1

            self.counter_null = 0






