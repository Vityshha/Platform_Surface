import traceback
from threading import Timer


# Класс реализующий сбрасывающийся таймер
# noinspection PyBroadException
class ResettableTimer(object):

    # Конструктор класса
    def __init__(self, interval, function):
        self.interval = interval
        self.function = function
        self.timer = Timer(self.interval, self.function)

    # Запуск таймера
    def run(self):
        self.timer.start()

    # Сброс таймера
    def reset(self):
        self.timer.cancel()
        self.timer = Timer(self.interval, self.function)
        self.timer.start()

    # Остановка и уничтожение таймера
    def destroy(self):
        try:
            self.timer.cancel()
            self.timer.join()
        except BaseException:
            traceback.print_exc()