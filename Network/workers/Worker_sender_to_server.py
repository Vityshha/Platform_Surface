import socket
from Network.sockets import NetworkConstants
from Enums.State_scenario import State_scenario
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot


class Worker_sender_to_server(QtCore.QObject):

    def __init__(self):
        super().__init__()
        self.buffer_size = 1024
        self.message = ""


    @Slot(int)
    def send_scenario(self, scenario):
        message = "0, " + str(scenario)
        self.send_message(message)

    @Slot(str)
    def send_trajectory(self, trajectory):
        message = trajectory
        self.send_message(message)

    @Slot(int)
    def send_sonar_chek(self, check):
        if check == 0:
            message = '3, 1' #Включен
        else:
            message = '3, 0' #Выключен
        self.send_message(message)

    @Slot(int, int)
    def send_position(self, x, y):
        message = '2, ' + str(x) + ', ' + str(y)
        self.send_message(message)

    def send_message(self, message):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect(NetworkConstants.SERVER_ADDRES_PORT)
        except:
            print('bad connection')
            return
        print("send to server message : '" + message + "'")
        self.socket.sendall(bytes(f"{message}", encoding="utf-8"))
        self.socket.close()
        self.socket = None