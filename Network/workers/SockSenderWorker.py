import struct
import traceback

from Network.sockets import NetworkConstants
import time

from Network.sockets.SockSender import ControllerSender
from PyQt5 import QtCore


# Класс обработки отправщика
# noinspection PyBroadException
class SenderWorker(QtCore.QObject):
    # Индикатор работы сокета отпарввщика
    sndIsRunning = False
    # Сокет отправщика
    sndSock = None

    # Таймер отправки данных управления
    vehicleSndTimer = None

    # Пакет данных техники
    vehicleData = None

    vehicleGas = 0
    vehicleWheel = 0
    vehicleBreak = 0
    vehicleHandBreak = 0
    vehicleLT = 0
    vehicleRT = 0

    # Constructor
    def __init__(self):
        super().__init__()
        self.sndSock = ControllerSender()

    # Основная функция работы в потоке
    def doWork(self):
        self.sndIsRunning = True
        self.vehicleSndTimer = QtCore.QTimer()
        self.vehicleSndTimer.timeout.connect(self.sendToVehicle)
        self.vehicleSndTimer.start(250)

    @QtCore.pyqtSlot()
    # Приостановка отправки данных на сервер
    def stopSender(self):
        self.vehicleSndTimer.stop()
        self.sndIsRunning = False

    @QtCore.pyqtSlot(int)
    # Включение отправки данных на сервер
    def startSender(self, uwu):
        self.vehicleSndTimer.start(250)
        self.sndIsRunning = True

    # Отправка данных
    def sendToVehicle(self):
        if self.sndSock is not None and self.sndIsRunning:
            try:
                self.sndSock.sendMessage(self.getDataToSend(), NetworkConstants.VEHICLE_ADDRESS_PORT)
            except BaseException:
                print("[e] Error in send to tractor")
                traceback.print_exc()

    def getDataToSend(self):
        veh_break = struct.unpack("<2B", struct.pack("<h", self.vehicleBreak))
        self.vehicleData = struct.pack(
            '<cB4b3Bc',
            b'#',
            1,
            self.vehicleGas,
            self.vehicleWheel,
            self.vehicleLT,
            self.vehicleRT,
            *veh_break,
            self.vehicleHandBreak,
            b'*'
        )
        return self.vehicleData

    # Слот обработка сигнала тормоза
    @QtCore.pyqtSlot(bool)
    def onBreak(self, pressed):
        self.vehicleBreak = 1 if pressed else 0
        print(f"{self.vehicleGas} {self.vehicleWheel} {self.vehicleLT} {self.vehicleRT} {self.vehicleBreak} {self.vehicleHandBreak}")

    @QtCore.pyqtSlot(bool)
    def onHandBreak(self, pressed):
        self.vehicleHandBreak = 1 if pressed else 0
        print(f"{self.vehicleGas} {self.vehicleWheel} {self.vehicleLT} {self.vehicleRT} {self.vehicleBreak} {self.vehicleHandBreak}")

    # Слот обработки сигнала нажатия на тормоз
    @QtCore.pyqtSlot()
    def onBreakPressed(self):
        self.vehicleBreak = 1
        print(f"{self.vehicleGas} {self.vehicleWheel} {self.vehicleLT} {self.vehicleRT} {self.vehicleBreak} {self.vehicleHandBreak}")

    # Слот обработки сигнала отжатия тормоза
    @QtCore.pyqtSlot()
    def onBreakReleased(self):
        self.vehicleBreak = 0
        print(f"{self.vehicleGas} {self.vehicleWheel} {self.vehicleLT} {self.vehicleRT} {self.vehicleBreak} {self.vehicleHandBreak}")

    # Слот обработки сигнала нажатия на газ
    @QtCore.pyqtSlot(int)
    def onGas(self, value):
        if -100 <= value <= 100:
            self.vehicleGas = value
            print(f"{self.vehicleGas} {self.vehicleWheel} {self.vehicleLT} {self.vehicleRT} {self.vehicleBreak} {self.vehicleHandBreak}")

    # Слот обработки сигнала поворота руля
    @QtCore.pyqtSlot(int)
    def onWheel(self, value):
        if -100 <= value <= 100:
            self.vehicleWheel = value
            print(f"{self.vehicleGas} {self.vehicleWheel} {self.vehicleLT} {self.vehicleRT} {self.vehicleBreak} {self.vehicleHandBreak}")

    @QtCore.pyqtSlot(int)
    def onRT(self, value):
        self.vehicleRT = value
        print(f"{self.vehicleGas} {self.vehicleWheel} {self.vehicleLT} {self.vehicleRT} {self.vehicleBreak} {self.vehicleHandBreak}")

    @QtCore.pyqtSlot(int)
    def onLT(self, value):
        self.vehicleLT = value
        print(f"{self.vehicleGas} {self.vehicleWheel} {self.vehicleLT} {self.vehicleRT} {self.vehicleBreak} {self.vehicleHandBreak}")
