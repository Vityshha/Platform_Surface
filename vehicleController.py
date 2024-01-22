from Network.workers.SockSenderWorker import SenderWorker
from PyQt5.QtCore import QThread, QObject
from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot

from Widget_settings.main_window import Main_Window
from Network.workers.Camera import Video_Thread
from Network.workers.Worker_sender_to_server import Worker_sender_to_server
import Network.sockets.NetworkConstants as Constants
from Network.workers.server_receiver_worker import ServerReceiverWorker
from Enums.State_scenario import State_scenario as STATE_SC

from Network.models.XboxProcess import XboxProcess



class MainWindow_Controller(QObject):
    send_com_signal_wheel = Signal(int)
    send_com_signal_gas = Signal(int)
    send_com_onLT_signal = Signal(int)
    send_com_onRT_signal = Signal(int)
    signal_surf_no_control = Signal()
    signal_take_surface_control = Signal(int)

    def __init__(self):
        super().__init__()

        self.ui = Main_Window()
        self.const = Constants
        self.server_receiver_worker = ServerReceiverWorker()
        self.server_receiver_thread = QThread()
        self.server_receiver_worker.moveToThread(self.server_receiver_thread)
        self.server_receiver_thread.started.connect(self.server_receiver_worker.do_work)
        self.server_receiver_thread.start()

        if self.const.isLocal:
            self.ui.showFullScreen()
            self.ui.show()
        else:
            # для того чтобы было в полное окно и не меняла ориентацию
            self.ui.showFullScreen()
            self.ui.show()
            self.ui.setFixedSize(self.ui.width(), self.ui.height())


        self.sndWorker = SenderWorker()
        self.video = Video_Thread(self.const.CAMERA_RTSP_ADDRES)
        self.sndServerWorker = Worker_sender_to_server()
        self.XboxProcess = XboxProcess()

        self.sndServerThread = QThread()
        self.sndThread = QThread()
        self.rcvThread = QThread()
        self.uiThread = QThread()

        self.sndWorker.moveToThread(self.sndThread)
        self.sndThread.started.connect(self.sndWorker.doWork)
        self.sndThread.start()
        self.sndServerWorker.moveToThread(self.sndServerThread)
        self.sndServerThread.start()
        self.ui.moveToThread(self.uiThread)
        self.uiThread.start()

        self.rcvThread.start()


        #для окна
        self.ui.joystick.send_com_signal_wheel.connect(self.sndWorker.onWheel)
        self.ui.joystick.send_com_signal_gas.connect(self.sndWorker.onGas)
        self.ui.joystick.send_com_onLT_signal.connect(self.sndWorker.onLT)
        self.ui.joystick.send_com_onRT_signal.connect(self.sndWorker.onRT)

        self.server_receiver_worker.receiver.signal_send_data_to_mapPaint.connect(self.ui.Paint.setPosPlatform)
        # self.server_receiver_worker.receiver.signal_send_bboxes.connect(self.ui.paint_rectangle)
        self.server_receiver_worker.receiver.signal_scenario_ended.connect(self.ui.disconnect_scenarios)
        self.server_receiver_worker.receiver.signal_scenario_ended.connect(self.sndWorker.startSender)

        self.video.send_vid.connect(self.ui.back_image)
        self.ui.signal_send_packages_to_server.connect(self.sndServerWorker.send_scenario)
        self.ui.signal_send_position_click.connect(self.sndServerWorker.send_position)
        self.ui.Paint.signal_send_trajectory.connect(self.sndServerWorker.send_trajectory)


        self.ui.ui.btn_circle.toggled.connect(self.stop_scenario_circle)
        self.ui.ui.btn_infin.toggled.connect(self.stop_scenario_infin)
        self.ui.ui.btn_trajectory.toggled.connect(self.stop_scenario_trajectory)
        self.ui.dialog.ui.btn_human.toggled.connect(self.stop_scenario_human)
        self.ui.dialog.ui.btn_target.toggled.connect(self.stop_scenario_target)
        self.ui.ui.btn_power.clicked.connect(self.close_app)

        self.signal_take_surface_control.connect(self.sndWorker.startSender)
        self.signal_take_surface_control.connect(self.sndServerWorker.send_scenario)
        self.signal_surf_no_control.connect(self.sndWorker.stopSender)
        self.ui.signal_close_event.connect(self.close_app)
        self.ui.signal_send_sonar.connect(self.sndServerWorker.send_sonar_chek)

        self.ui.ui.btn_stick.toggled.connect(self.gamepade_mode)

        self.ui.ui.btn_circle.toggled.connect(self.disconnect_joy)
        self.ui.ui.btn_eyes.toggled.connect(self.disconnect_joy)
        self.ui.ui.btn_infin.toggled.connect(self.disconnect_joy)
        self.ui.ui.btn_map.toggled.connect(self.disconnect_joy)

    def stop_scenario_circle(self):
        if self.ui.ui.btn_circle.isChecked():
            self.signal_surf_no_control.emit()
        else:
            self.signal_take_surface_control.emit(0)
    def stop_scenario_infin(self):
        if self.ui.ui.btn_infin.isChecked():
            self.signal_surf_no_control.emit()
        else:
            self.signal_take_surface_control.emit(0)
    def stop_scenario_trajectory(self):
        if self.ui.ui.btn_trajectory.isChecked():
            self.signal_surf_no_control.emit()
        else:
            self.signal_take_surface_control.emit(0)
    def stop_scenario_target(self):
        if self.ui.dialog.ui.btn_target.isChecked():
            self.signal_surf_no_control.emit()
        else:
            self.signal_take_surface_control.emit(0)
    def stop_scenario_human(self):
        if self.ui.dialog.ui.btn_human.isChecked():
            self.signal_surf_no_control.emit()
        else:
            self.signal_take_surface_control.emit(0)

    def gamepade_mode(self):
        button = [self.ui.ui.btn_eyes.isChecked(), self.ui.ui.btn_infin.isChecked(), self.ui.ui.btn_circle.isChecked()]
        if self.ui.ui.btn_stick.isChecked():
            if True in button:
                self.ui.ui.stackedWidget.setCurrentIndex(1)
            else:
                self.reconnect()
        else:
            if True in button:
                self.ui.ui.stackedWidget.setCurrentIndex(1)
            try:
                self.disconnect_j()
                self.ui.ui.stackedWidget.setCurrentIndex(0)
            except:
                return

    def disconnect_joy(self, checked):
        if not self.ui.ui.btn_stick.isChecked() and checked:
            self.ui.ui.stackedWidget.setCurrentIndex(1)
        elif self.ui.ui.btn_stick.isChecked() and not checked:
            if not self.ui.ui.btn_map.isChecked():
                self.reconnect()
            else:
                self.ui.ui.stackedWidget.setCurrentIndex(0)
        elif self.ui.ui.btn_stick.isChecked() and checked:
            try:
                self.disconnect_j()
            except:
                return
        else:
            self.ui.ui.stackedWidget.setCurrentIndex(0)

    def disconnect_j(self):
        self.ui.ui.stackedWidget.setCurrentIndex(1)
        self.XboxProcess.gamepad.gasChanged.disconnect(self.sndWorker.onGas)
        self.XboxProcess.gamepad.breakChanged.disconnect(self.sndWorker.onBreak)
        self.XboxProcess.gamepad.handbreakChanged.disconnect(self.sndWorker.onHandBreak)
        self.XboxProcess.gamepad.ltChanged.disconnect(self.sndWorker.onLT)
        self.XboxProcess.gamepad.rtChanged.disconnect(self.sndWorker.onRT)

    def reconnect(self):
        self.ui.ui.stackedWidget.setCurrentIndex(1)
        self.XboxProcess.gamepad.gasChanged.connect(self.sndWorker.onGas)
        self.XboxProcess.gamepad.breakChanged.connect(self.sndWorker.onBreak)
        self.XboxProcess.gamepad.handbreakChanged.connect(self.sndWorker.onHandBreak)
        self.XboxProcess.gamepad.ltChanged.connect(self.sndWorker.onLT)
        self.XboxProcess.gamepad.rtChanged.connect(self.sndWorker.onRT)

    @Slot()
    def close_app(self):
        self.ui.signal_send_packages_to_server.emit(STATE_SC.CONTROL_BY_SURFACE.value)
        self.sndThread.quit()
        self.sndThread.wait()

        self.uiThread.quit()
        self.uiThread.wait()

        self.rcvThread.quit()
        self.rcvThread.wait()
        self.ui.close()