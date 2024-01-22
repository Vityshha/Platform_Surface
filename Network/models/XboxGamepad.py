# Нужен модуль XInput установка командой: "pip install XInput-Python"
import time

from XInput import *
from PyQt5.QtCore import QObject, pyqtSignal, QMutexLocker, QMutex


# Класс состояния геймпада, обработчик данных геймпада
class XboxGamepad(EventHandler, QObject):
    # Обработка нажатия на кнопку тормоза
    breakChanged = pyqtSignal(bool)
    handbreakChanged = pyqtSignal(bool)
    # Обработка изменения статуса соединения
    connectionStatusChanged = pyqtSignal(bool)
    signalDisconnect = pyqtSignal(bool)
    signalConnect = pyqtSignal(bool)
    # Обработка изменения состояния газа
    gasChanged = pyqtSignal(int)
    # Обработка изменения состояния руля
    wheelAngleChanged = pyqtSignal(int)
    rtChanged = pyqtSignal(int)
    ltChanged = pyqtSignal(int)

    # Стрелочки
    ARROW_UP = 0
    ARROW_DOWN = 0
    ARROW_LEFT = 0
    ARROW_RIGHT = 0

    # Буквенные кнопки
    A = 0
    B = 0
    Y = 0
    X = 0

    # Кнопки около курков
    LB = 0
    RB = 0

    # Курки
    LT = 0
    RT = 0

    # Левый стик
    STICK_LX = 0
    STICK_LY = 0

    # Правый стик
    STICK_RX = 0
    STICK_RY = 0

    # Кнопка левого стика
    STICK_L_BTN = 0

    # Кнопка правого стика
    STICK_R_BTN = 0

    hb = True

    # Индикатор соединения с геймпадом
    isConnected = False

    # Конструктор
    def __init__(self, num):
        EventHandler.__init__(self, num)
        QObject.__init__(self)
        self.mutex = QMutex()

    # Сброс данных
    def resetData(self):
        # Gamepad
        self.ARROW_UP = 0
        self.ARROW_DOWN = 0
        self.ARROW_LEFT = 0
        self.ARROW_RIGHT = 0
        self.A = 0
        self.B = 0
        self.Y = 0
        self.X = 0
        self.LB = 0
        self.RB = 0
        self.LT = 0
        self.RT = 0
        self.STICK_LX = 0
        self.STICK_LY = 0
        self.STICK_RX = 0
        self.STICK_RY = 0
        self.STICK_L_BTN = 0
        self.STICK_R_BTN = 0
        if self.A == 0:
            self.breakChanged.emit(False)
        else:
            self.breakChanged.emit(True)
        self.gasChanged.emit(self.STICK_LY)
        self.wheelAngleChanged.emit(self.STICK_RX)

        self.hb = True

    # Печать в потоке вывода состояния элементов геймпада
    def printState(self):
        print('ARROW_UP', self.ARROW_UP)
        print('ARROW_DOWN', self.ARROW_DOWN)
        print('ARROW_LEFT', self.ARROW_LEFT)
        print('ARROW_RIGHT', self.ARROW_RIGHT)
        print('A', self.A)
        print('B', self.B)
        print('Y', self.Y)
        print('X', self.X)
        print('LB', self.LB)
        print('RB', self.RB)
        print('LT', self.LT)
        print('RT', self.RT)
        print('STICK_LX', self.STICK_LX)
        print('STICK_LY', self.STICK_LY)
        print('STICK_RX', self.STICK_RX)
        print('STICK_RY', self.STICK_RY)
        print('STICK_L_BTN', self.STICK_L_BTN)
        print('STICK_R_BTN', self.STICK_R_BTN)

    # Обработчик событий нажатия на кнопки геймпада
    def process_button_event(self, event):
        if event.type == EVENT_BUTTON_PRESSED:
            if event.button == "LEFT_THUMB":
                self.STICK_L_BTN = 1
            elif event.button == "RIGHT_THUMB":
                self.STICK_R_BTN = 1
            elif event.button == "LEFT_SHOULDER":
                self.LB = 1
            elif event.button == "RIGHT_SHOULDER":
                self.RB = 1
            elif event.button == "DPAD_LEFT":
                self.ARROW_LEFT = 1
            elif event.button == "DPAD_RIGHT":
                self.ARROW_RIGHT = 1
            elif event.button == "DPAD_UP":
                self.ARROW_UP = 1
            elif event.button == "DPAD_DOWN":
                self.ARROW_DOWN = 1
            elif event.button == "A":
                self.A = 1
                self.breakChanged.emit(True)
            elif event.button == "B":
                self.B = 1
            elif event.button == "Y":
                self.Y = 1
                self.handbreakChanged.emit(self.hb)
                self.hb = not self.hb
            elif event.button == "X":
                self.X = 1
        elif event.type == EVENT_BUTTON_RELEASED:
            if event.button == "LEFT_THUMB":
                self.STICK_L_BTN = 0
            elif event.button == "RIGHT_THUMB":
                self.STICK_R_BTN = 0
            elif event.button == "LEFT_SHOULDER":
                self.LB = 0
            elif event.button == "RIGHT_SHOULDER":
                self.RB = 0
            elif event.button == "DPAD_LEFT":
                self.ARROW_LEFT = 0
            elif event.button == "DPAD_RIGHT":
                self.ARROW_RIGHT = 0
            elif event.button == "DPAD_UP":
                self.ARROW_UP = 0
            elif event.button == "DPAD_DOWN":
                self.ARROW_DOWN = 0
            elif event.button == "A":
                self.A = 0
                self.breakChanged.emit(False)
            elif event.button == "B":
                self.B = 0
            elif event.button == "Y":
                self.Y = 0
            elif event.button == "X":
                self.X = 0

    # Обработчик событий стиков
    def process_stick_event(self, event):
        if event.type == EVENT_STICK_MOVED:
            if event.stick == LEFT:
                self.STICK_LX = round(event.x * 100)
                self.STICK_LY = round(event.y * 100)
                self.gasChanged.emit(self.STICK_LY)
            elif event.stick == RIGHT:
                self.STICK_RX = round(event.x * 100)
                self.STICK_RY = round(event.y * 100)
                self.wheelAngleChanged.emit(self.STICK_RX)

    # Обработчик событий курков
    def process_trigger_event(self, event):
        if event.type == EVENT_TRIGGER_MOVED:
            if event.trigger == LEFT:
                self.LT = round(event.value * 100)
                self.ltChanged.emit(self.LT)
            elif event.trigger == RIGHT:
                self.RT = round(event.value * 100)
                self.rtChanged.emit(self.RT)

    # Обработчик событий подключения
    def process_connection_event(self, event):
        with QMutexLocker(self.mutex):
            if event.type == EVENT_CONNECTED:
                self.isConnected = True
                print("Connected")
            elif event.type == EVENT_DISCONNECTED:
                self.isConnected = False
                self.resetData()
                print("Disconnected")