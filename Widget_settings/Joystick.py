from enum import Enum
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QPointF, QRectF, QLineF
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import pyqtSignal as Signal


class Direction(Enum):
    Left = 0
    Right = 1
    Up = 2
    Down = 3

class Joystick(QWidget):

    send_com_signal_wheel = Signal(int)
    send_com_signal_gas = Signal(int)
    send_com_onLT_signal = Signal(int)
    send_com_onRT_signal = Signal(int)

    def __init__(self, parent=None):
        super(Joystick, self).__init__(parent)
        self.movingOffset = QPointF(0, 0)
        self.grabCenter = False
        self.__maxDistance = 200
        self.size_nipple = 100
        self.press = True

    # Рисует джостик
    def paintEvent(self, event):
        if self.grabCenter:
            painter = QPainter(self)
            bounds = QRectF(-self.__maxDistance, -self.__maxDistance, self.__maxDistance * 2,
                            self.__maxDistance * 2).translated(self._center())
            painter.setPen(QPen(QColor(182, 182, 182), 0))
            painter.setBrush(QColor(182, 182, 182))
            painter.drawEllipse(bounds)

            if self.grabCenter:
                painter.setPen(QPen(QColor(169, 169, 169), self.size_nipple))
                painter.drawEllipse(self._centerEllipse())

    # Определения захвата центра
    def _centerEllipse(self):
        if self.grabCenter:
            return QRectF(-80, -80, 100, 100).translated(self.movingOffset)
        return QRectF(-80, -80, 100, 100).translated(self._center())

    # Определение центра виджета
    def _center(self):
        x = self.coord.x()
        y = self.coord.y()
        return QPointF(x, y)

     # Ограничение перемещения джостика
    def _boundJoystick(self, point):
        limitLine = QLineF(self._center(), point)
        if (limitLine.length() > self.__maxDistance):
            limitLine.setLength(self.__maxDistance)
        return limitLine.p2()

    # Определение направления джостика
    def joystickDirection(self):
        if not self.grabCenter:
            return 0
        normVector = QLineF(self._center(), self.movingOffset)
        currentDistance = normVector.length()
        angle = normVector.angle()

        distance = min(currentDistance / self.__maxDistance, 1.0)
        if 45 <= angle < 135:
            return (Direction.Up, distance)
        elif 135 <= angle < 225:
            return (Direction.Left, distance)
        elif 225 <= angle < 315:
            return (Direction.Down, distance)
        return (Direction.Right, distance)

    def mousePressEvent(self, ev):
        if not self.grabCenter:
            if self.press:
                self.coord = ev.pos()
            self.movingOffset = self._boundJoystick(ev.pos())
            self.press = True
            self.grabCenter = True
            self.update()

    def mouseReleaseEvent(self, event):
        self.grabCenter = False
        self.press = True
        self.movingOffset = QPointF(0, 0)
        message = ('abc.abc', 0)
        self.send_command(message)
        self.update()

    def mouseMoveEvent(self, ev):
        if self.grabCenter:
            self.movingOffset = self._boundJoystick(ev.pos())
            direct, radius = self.joystickDirection()[0], self.joystickDirection()[1]
            direct = str(direct)
            message = (direct, radius)
            self.send_command(message)
            self.update()

    def send_command(self, data):
        if data[0].split('.')[1] == 'Up':
            self.send_com_signal_gas.emit(int(data[1] * 100))
            self.send_com_onRT_signal.emit(0)
            self.send_com_onLT_signal.emit(0)
        elif data[0].split('.')[1] == 'Down':
            self.send_com_signal_gas.emit(int(data[1] * -100))
            self.send_com_onRT_signal.emit(0)
            self.send_com_onLT_signal.emit(0)
        elif data[0].split('.')[1] == 'Left':
            self.send_com_onLT_signal.emit(int(data[1] * 100))
            self.send_com_signal_gas.emit(0)
            self.send_com_onRT_signal.emit(0)
        elif data[0].split('.')[1] == 'Right':
            self.send_com_onRT_signal.emit(int(data[1] * 100))
            self.send_com_signal_gas.emit(0)
            self.send_com_onLT_signal.emit(0)
        else:
            self.send_com_signal_gas.emit(0)
            self.send_com_onLT_signal.emit(0)
            self.send_com_onRT_signal.emit(0)


