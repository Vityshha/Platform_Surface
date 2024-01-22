from XInput import *
from Network.models.XboxGamepad import XboxGamepad
from PyQt5.QtCore import QThread

# Основной класс для работы с геймпадом
class XboxProcess(QThread):
    thread = None
    gamepad = None
    isRunning = False

    def __init__(self):
        super().__init__()
        set_deadzone(DEADZONE_TRIGGER, 10)
        # Важный момент - геймпадов может быть много на устройстве, мы используем первый попавшийся!!!!
        self.gamepad = XboxGamepad(0)
        self.thread = GamepadThread(self.gamepad)
        self.isRunning = True
        #todo мега плохо, но работает  без лагов:)
        self.thread.start()
        time.sleep(0.01)
        self.thread.start()
