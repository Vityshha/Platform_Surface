import sys

from PyQt5.QtGui import QPixmap, QBrush, QPen
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsItem
from PyQt5.QtCore import Qt, pyqtProperty


class Platform(QGraphicsRectItem):

    platform_image_path = 'UI/icons//platform_image.png'

    def __init__(self, x, y, width, height):
        super().__init__(0, 0, width, height)
        self.setPos(x, y)

        self.setPen(QPen(Qt.NoPen))
        pixmap = QPixmap(self.platform_image_path)
        brush = QBrush(pixmap)
        self.setBrush(brush)
        self.setScale(0.9)
        self.setAcceptHoverEvents(True)
        self.setTransformOriginPoint(0, height/2)
        self.flag = True
        self.last_mouse_pos = None

    # mouse hover event
    def hoverEnterEvent(self, event):
        #app.instance().setOverrideCursor(Qt.OpenHandCursor)
        pass

    def hoverLeaveEvent(self, event):
        #app.instance().restoreOverrideCursor()
        pass
    # mouse click event
    def mousePressEvent(self, event):
        self.last_mouse_pos = event.scenePos()

    def mouseMoveEvent(self, event):
        if self.flag and self.last_mouse_pos:
            new_mouse_pos = event.scenePos()
            delta = new_mouse_pos - self.last_mouse_pos
            self.last_mouse_pos = new_mouse_pos
            self.moveBy(delta.x(), delta.y())

    def mouseReleaseEvent(self, event):
        #print('x: {0}, y: {1}'.format(self.pos().x(), self.pos().y()))
        self.last_mouse_pos = None



class GraphicView(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setSceneRect(0, 0, 1200, 1000)

        self.moveObject = Platform(10, 100, 318, 140)
        self.scene.addItem(self.moveObject)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = GraphicView()
    view.show()
    sys.exit(app.exec_())