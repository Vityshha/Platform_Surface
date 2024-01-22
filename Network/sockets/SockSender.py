import socket
import traceback


# Класс пересыльщик данных на трактор при помощи дейтограммных сокетов
# noinspection PyBroadException
class ControllerSender:
    # Сокет
    sock = None

    # Конструктор класса
    def __init__(self):
        self.sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Функция отправки данных
    def sendMessage(self, messageInBytes, address):
        try:
            if self.sock is not None:
                self.sock.sendto(messageInBytes, address)
        except BaseException:
            print("[e] Failed to send data")
            traceback.print_exc()