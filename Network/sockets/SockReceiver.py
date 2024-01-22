import socket
import traceback
import importlib
from PyQt5.QtCore import QObject, pyqtSignal as Signal
from Network.sockets import NetworkConstants


# Класс дейтаграммного приемника
# noinspection PyBroadException
class ControllerReceiver(QObject):
    # ------------------ FIELDS-------------------------
    # Сокет
    sock = None
    # Сетевой адрес
    # address = None
    # Буфер сообщения
    messageBuffer = None
    # Данные с трактора
    vehicleResponseData = None

    first_start = True

    signal_send_data_to_mapPaint = Signal(list)
    signal_scenario_ended = Signal(int)
    signal_send_bboxes = Signal(list)



    # -------------------- METHODS -----------------------
    # Constructor
    def __init__(self):
        QObject.__init__(self)
        self.switch_startup()
        address = NetworkConstants.CONTROLLER_ADDRESS_PORT
        self.sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        try:
            self.sock.bind(address)
        except:
            self.switch_startup()
            importlib.reload(NetworkConstants)
            address = NetworkConstants.CONTROLLER_ADDRESS_PORT
            self.sock.bind(address)

        self.address = address

    # Функция приема данных
    def receiveData(self):
        try:
            self.messageBuffer = self.sock.recvfrom(8192)[0]
            if self.messageBuffer is not None:
                msg = self.messageBuffer.decode('utf-8').split(' ')
                msg = [int(byte) for byte in msg]
               # print('message', msg, type(msg))

                if msg[0] == 0:
                    self.signal_send_data_to_mapPaint.emit(list(msg))
                elif msg[0] == 1:
                    self.signal_send_bboxes.emit(msg[1:])
                elif msg[0] == 2:
                    self.signal_scenario_ended.emit(0)
                else:
                    return
            else:
                return
        except BaseException:
            print("[e] Error with")
            traceback.print_exc()
            self.sock.close()
            self.messageBuffer = None
            self.sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            self.sock.bind(self.address)

    # Идентификация пакета
    def getHeader(self):
        if self.messageBuffer is not None:
            msg = self.messageBuffer.decode("utf-8").split(", ")
            if msg[0] == 0:
                self.signal_send_data_to_mapPaint.emit(msg[1:])
            elif msg[0] == 1:
                self.signal_send_bboxes.emit(msg[1:])
            elif msg[0] == 2:
                self.signal_scenario_ended.emit(0)
            else:
                return
        else:
            return


    def switch_startup(self):
        file_path = 'Network/sockets/NetworkConstants.py'
        line_number = 2
        if self.first_start:
            new_line = "isLocal = False \n"
            self.first_start = False
        else:
            new_line = "isLocal = True \n"

        with open(file_path, 'r') as file:
            lines = file.readlines()
        lines[line_number - 1] = new_line
        with open(file_path, 'w') as file:
            file.writelines(lines)
