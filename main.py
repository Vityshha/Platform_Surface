import sys
from PyQt5.QtWidgets import QApplication
from vehicleController import MainWindow_Controller

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow_Controller()
    app = app.exec_()
    sys.exit(app)