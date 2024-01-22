from PyQt5.QtCore import QThread, QObject
from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
from Network.sockets.SockReceiver import ControllerReceiver


class ServerReceiverWorker(QObject):
    def __init__(self):
        super().__init__()
        self.receiver = ControllerReceiver()

    def do_work(self):
        while True:
            self.receiver.receiveData()