# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(977, 682)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(147, 147, 147);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("border: none;\n"
"background: transparent;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.menu_frame = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_frame.sizePolicy().hasHeightForWidth())
        self.menu_frame.setSizePolicy(sizePolicy)
        self.menu_frame.setStyleSheet("border: none;\n"
"background: transparent;")
        self.menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_frame.setObjectName("menu_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.menu_frame)
        self.gridLayout.setContentsMargins(10, 10, 10, 0)
        self.gridLayout.setHorizontalSpacing(13)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_power = QtWidgets.QPushButton(self.menu_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_power.sizePolicy().hasHeightForWidth())
        self.btn_power.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_power.setFont(font)
        self.btn_power.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 6px;\n"
"    /*background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);*/\n"
"    \n"
"    background-color: rgba(62, 63, 70, 0.7);\n"
"\n"
"    min-width: 80px;\n"
"    image: url(UI/icons/power.svg);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"")
        self.btn_power.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/power.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_power.setIcon(icon)
        self.btn_power.setIconSize(QtCore.QSize(26, 26))
        self.btn_power.setCheckable(True)
        self.btn_power.setObjectName("btn_power")
        self.gridLayout.addWidget(self.btn_power, 0, 0, 1, 1)
        self.btn_camera = QtWidgets.QPushButton(self.menu_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_camera.sizePolicy().hasHeightForWidth())
        self.btn_camera.setSizePolicy(sizePolicy)
        self.btn_camera.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(30)
        self.btn_camera.setFont(font)
        self.btn_camera.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 6px;\n"
"    background-color:  rgba(62, 63, 70, 0.7);\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgba(217, 217, 217, 0.7);\n"
"    color: rgb(21, 21, 21);\n"
"}")
        self.btn_camera.setCheckable(True)
        self.btn_camera.setChecked(True)
        self.btn_camera.setObjectName("btn_camera")
        self.gridLayout.addWidget(self.btn_camera, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.btn_map = QtWidgets.QPushButton(self.menu_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_map.sizePolicy().hasHeightForWidth())
        self.btn_map.setSizePolicy(sizePolicy)
        self.btn_map.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(30)
        self.btn_map.setFont(font)
        self.btn_map.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(62, 63, 70, 0.7);\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgba(217, 217, 217, 0.7);\n"
"    color: rgb(21, 21, 21);\n"
"}\n"
"")
        self.btn_map.setCheckable(True)
        self.btn_map.setObjectName("btn_map")
        self.gridLayout.addWidget(self.btn_map, 0, 3, 1, 1)
        self.stackedWidget_btn = QtWidgets.QStackedWidget(self.menu_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_btn.sizePolicy().hasHeightForWidth())
        self.stackedWidget_btn.setSizePolicy(sizePolicy)
        self.stackedWidget_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget_btn.setAcceptDrops(True)
        self.stackedWidget_btn.setObjectName("stackedWidget_btn")
        self.page_eyes = QtWidgets.QWidget()
        self.page_eyes.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.page_eyes.setObjectName("page_eyes")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_eyes)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_eyes = QtWidgets.QPushButton(self.page_eyes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_eyes.sizePolicy().hasHeightForWidth())
        self.btn_eyes.setSizePolicy(sizePolicy)
        self.btn_eyes.setMinimumSize(QtCore.QSize(84, 0))
        self.btn_eyes.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_eyes.setFont(font)
        self.btn_eyes.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(62, 63, 70, 0.7);\n"
"    image: url(UI/icons/eyes.svg);\n"
"    min-width: 80px;\n"
"    }\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid rgba(217, 217, 217, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(217, 217, 217, 0.7);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_eyes.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/eyes.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_eyes.setIcon(icon1)
        self.btn_eyes.setIconSize(QtCore.QSize(25, 25))
        self.btn_eyes.setCheckable(True)
        self.btn_eyes.setObjectName("btn_eyes")
        self.verticalLayout_5.addWidget(self.btn_eyes)
        self.stackedWidget_btn.addWidget(self.page_eyes)
        self.page_settings = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_settings.sizePolicy().hasHeightForWidth())
        self.page_settings.setSizePolicy(sizePolicy)
        self.page_settings.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.page_settings.setObjectName("page_settings")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_settings)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.btn_settings = QtWidgets.QComboBox(self.page_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(59)
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setMinimumSize(QtCore.QSize(84, 0))
        self.btn_settings.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_settings.setFont(font)
        self.btn_settings.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_settings.setAutoFillBackground(False)
        self.btn_settings.setStyleSheet("QComboBox {\n"
"    border: 2px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(62, 63, 70, 0.7);\n"
"    image: url(UI/icons/settings.svg);\n"
"    color: transparent;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"    background-color: rgba(217, 217, 217, 0.7);\n"
"    image: url(UI/icons/expand.svg);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(147, 147, 147, 0.5);\n"
"    min-width: 600;\n"
"    selection-background-color: rgba(217, 217, 217, 1);\n"
"    selection-color: rgb(21, 21, 21);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"\n"
"    border-top: 10px solid black; /* Разделяющая линия сверху */\n"
"    border-bottom: 10px solid black; /* Разделяющая линия снизу */\n"
"    border-bottom-color: 10px rgb(3, 20, 255);\n"
"\n"
"}")
        self.btn_settings.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.btn_settings.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.btn_settings.setIconSize(QtCore.QSize(25, 25))
        self.btn_settings.setObjectName("btn_settings")
        self.btn_settings.addItem("")
        self.btn_settings.addItem("")
        self.btn_settings.addItem("")
        self.btn_settings.addItem("")
        self.btn_settings.addItem("")
        self.btn_settings.addItem("")
        self.btn_settings.addItem("")
        self.verticalLayout_9.addWidget(self.btn_settings)
        self.stackedWidget_btn.addWidget(self.page_settings)
        self.gridLayout.addWidget(self.stackedWidget_btn, 0, 5, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        self.verticalLayout_2.addWidget(self.menu_frame)
        self.stackedWidget_main = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget_main.setStyleSheet("border: none;\n"
"background: transparent;")
        self.stackedWidget_main.setObjectName("stackedWidget_main")
        self.page_camera = QtWidgets.QWidget()
        self.page_camera.setObjectName("page_camera")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_camera)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.management_widget = QtWidgets.QWidget(self.page_camera)
        self.management_widget.setStyleSheet("border: none;\n"
"background: transparent;")
        self.management_widget.setObjectName("management_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.management_widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stick_widget = QtWidgets.QWidget(self.management_widget)
        self.stick_widget.setStyleSheet("border: none;\n"
"background: transparent;")
        self.stick_widget.setObjectName("stick_widget")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.stick_widget)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_4 = QtWidgets.QFrame(self.stick_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.frame_4.setFont(font)
        self.frame_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_4.setStyleSheet("border: none;\n"
"background: transparent;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_13.setContentsMargins(0, 10, 10, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.formLayout = QtWidgets.QFormLayout(self.frame_6)
        self.formLayout.setContentsMargins(10, 0, 0, 0)
        self.formLayout.setSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(15)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.btn_infin = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_infin.sizePolicy().hasHeightForWidth())
        self.btn_infin.setSizePolicy(sizePolicy)
        self.btn_infin.setMinimumSize(QtCore.QSize(84, 0))
        self.btn_infin.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_infin.setFont(font)
        self.btn_infin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_infin.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(62, 63, 70, 0.7);\n"
"    image: url(UI/icons/triangle.svg);\n"
"    min-width: 80px;\n"
"    }\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid rgba(217, 217, 217, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(217, 217, 217, 0.7);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_infin.setText("")
        self.btn_infin.setIcon(icon1)
        self.btn_infin.setIconSize(QtCore.QSize(25, 25))
        self.btn_infin.setCheckable(True)
        self.btn_infin.setObjectName("btn_infin")
        self.verticalLayout_15.addWidget(self.btn_infin, 0, QtCore.Qt.AlignRight)
        self.btn_circle = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_circle.sizePolicy().hasHeightForWidth())
        self.btn_circle.setSizePolicy(sizePolicy)
        self.btn_circle.setMinimumSize(QtCore.QSize(84, 0))
        self.btn_circle.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_circle.setFont(font)
        self.btn_circle.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(62, 63, 70, 0.7);\n"
"    image: url(UI/icons/square.svg);\n"
"    min-width: 80px;\n"
"    }\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid rgba(217, 217, 217, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(217, 217, 217, 0.7);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_circle.setText("")
        self.btn_circle.setIcon(icon1)
        self.btn_circle.setIconSize(QtCore.QSize(25, 25))
        self.btn_circle.setCheckable(True)
        self.btn_circle.setObjectName("btn_circle")
        self.verticalLayout_15.addWidget(self.btn_circle, 0, QtCore.Qt.AlignRight)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(15)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.btn_sonar = QtWidgets.QPushButton(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sonar.sizePolicy().hasHeightForWidth())
        self.btn_sonar.setSizePolicy(sizePolicy)
        self.btn_sonar.setMinimumSize(QtCore.QSize(84, 0))
        self.btn_sonar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_sonar.setFont(font)
        self.btn_sonar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_sonar.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(62, 63, 70, 0.7);\n"
"    image: url(UI/icons/sensor.svg);\n"
"    min-width: 80px;\n"
"    }\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid rgba(217, 217, 217, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(217, 217, 217, 0.7);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_sonar.setText("")
        self.btn_sonar.setIcon(icon1)
        self.btn_sonar.setIconSize(QtCore.QSize(25, 25))
        self.btn_sonar.setCheckable(True)
        self.btn_sonar.setObjectName("btn_sonar")
        self.verticalLayout_17.addWidget(self.btn_sonar)
        self.btn_stick = QtWidgets.QPushButton(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_stick.sizePolicy().hasHeightForWidth())
        self.btn_stick.setSizePolicy(sizePolicy)
        self.btn_stick.setMinimumSize(QtCore.QSize(84, 0))
        self.btn_stick.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_stick.setFont(font)
        self.btn_stick.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_stick.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(62, 63, 70, 0.7);\n"
"    image: url(UI/icons/gamepade.svg);\n"
"    min-width: 80px;\n"
"    }\n"
"\n"
"QPushButton:checked {\n"
"    border: 2px solid rgba(217, 217, 217, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(217, 217, 217, 0.7);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_stick.setText("")
        self.btn_stick.setIcon(icon1)
        self.btn_stick.setIconSize(QtCore.QSize(25, 25))
        self.btn_stick.setCheckable(True)
        self.btn_stick.setObjectName("btn_stick")
        self.verticalLayout_17.addWidget(self.btn_stick)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame_8)
        self.verticalLayout_13.addWidget(self.frame_6)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_4)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_joystick = QtWidgets.QWidget(self.page)
        self.widget_joystick.setObjectName("widget_joystick")
        self.verticalLayout_7.addWidget(self.widget_joystick)
        self.stackedWidget.addWidget(self.page)
        self.no_joystick = QtWidgets.QWidget()
        self.no_joystick.setObjectName("no_joystick")
        self.stackedWidget.addWidget(self.no_joystick)
        self.verticalLayout_13.addWidget(self.stackedWidget)
        self.verticalLayout_12.addWidget(self.frame_4)
        self.gridLayout_2.addWidget(self.stick_widget, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.management_widget)
        self.stackedWidget_main.addWidget(self.page_camera)
        self.page_map = QtWidgets.QWidget()
        self.page_map.setObjectName("page_map")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_map)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 17)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.page_map)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.graphicsView = Paint(self.frame_5)
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.graphicsView.setInteractive(True)
        self.graphicsView.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.graphicsView.setAlignment(QtCore.Qt.AlignCenter)
        self.graphicsView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.SmoothPixmapTransform|QtGui.QPainter.TextAntialiasing)
        self.graphicsView.setTransformationAnchor(QtWidgets.QGraphicsView.NoAnchor)
        self.graphicsView.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)
        self.graphicsView.setOptimizationFlags(QtWidgets.QGraphicsView.DontAdjustForAntialiasing)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_6.addWidget(self.graphicsView)
        self.gridLayout_3.addWidget(self.frame_5, 2, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.page_map)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(23, 0, 10, 0)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_trajectory = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_trajectory.setFont(font)
        self.btn_trajectory.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 6px;\n"
"    /*background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);*/\n"
"    \n"
"    background-color: rgba(62, 63, 70, 0.7);\n"
"\n"
"    min-width: 80px;\n"
"    image: url(UI/icons/path.svg);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"")
        self.btn_trajectory.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_trajectory.setIcon(icon2)
        self.btn_trajectory.setIconSize(QtCore.QSize(25, 25))
        self.btn_trajectory.setCheckable(True)
        self.btn_trajectory.setChecked(False)
        self.btn_trajectory.setObjectName("btn_trajectory")
        self.verticalLayout_3.addWidget(self.btn_trajectory)
        self.stackedWidget_size = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget_size.setObjectName("stackedWidget_size")
        self.page_size_invis = QtWidgets.QWidget()
        self.page_size_invis.setObjectName("page_size_invis")
        self.stackedWidget_size.addWidget(self.page_size_invis)
        self.page_size_vis = QtWidgets.QWidget()
        self.page_size_vis.setObjectName("page_size_vis")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_size_vis)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.btn_plus = QtWidgets.QPushButton(self.page_size_vis)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(62, 63, 70, 0.7);\n"
"    min-width: 80px;\n"
"    image: url(UI/icons/add.svg);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid rgba(217, 217, 217, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(217, 217, 217, 0.7);\n"
"    min-width: 80px;\n"
"    image: url(UI/icons/add.svg);\n"
"}\n"
"\n"
"\n"
"")
        self.btn_plus.setText("")
        self.btn_plus.setIcon(icon2)
        self.btn_plus.setIconSize(QtCore.QSize(25, 25))
        self.btn_plus.setCheckable(True)
        self.btn_plus.setChecked(False)
        self.btn_plus.setObjectName("btn_plus")
        self.verticalLayout_11.addWidget(self.btn_plus)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem2)
        self.btn_remove = QtWidgets.QPushButton(self.page_size_vis)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_remove.setFont(font)
        self.btn_remove.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(62, 63, 70, 0.7);\n"
"    min-width: 80px;\n"
"    image: url(UI/icons/remove.svg);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid rgba(217, 217, 217, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(217, 217, 217, 0.7);\n"
"    min-width: 80px;\n"
"    image: url(UI/icons/remove.svg);\n"
"}\n"
"\n"
"\n"
"")
        self.btn_remove.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_remove.setIcon(icon3)
        self.btn_remove.setIconSize(QtCore.QSize(25, 25))
        self.btn_remove.setCheckable(True)
        self.btn_remove.setChecked(False)
        self.btn_remove.setObjectName("btn_remove")
        self.verticalLayout_11.addWidget(self.btn_remove)
        self.stackedWidget_size.addWidget(self.page_size_vis)
        self.page_scale = QtWidgets.QWidget()
        self.page_scale.setObjectName("page_scale")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_scale)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.btn_plus_scale = QtWidgets.QPushButton(self.page_scale)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_plus_scale.setFont(font)
        self.btn_plus_scale.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(62, 63, 70, 0.7);\n"
"    min-width: 80px;\n"
"    image: url(UI/icons/add.svg);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid rgba(217, 217, 217, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(217, 217, 217, 0.7);\n"
"    min-width: 80px;\n"
"    image: url(UI/icons/add.svg);\n"
"}\n"
"\n"
"\n"
"")
        self.btn_plus_scale.setText("")
        self.btn_plus_scale.setIcon(icon2)
        self.btn_plus_scale.setIconSize(QtCore.QSize(25, 25))
        self.btn_plus_scale.setCheckable(True)
        self.btn_plus_scale.setChecked(False)
        self.btn_plus_scale.setObjectName("btn_plus_scale")
        self.verticalLayout_8.addWidget(self.btn_plus_scale)
        spacerItem3 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem3)
        self.btn_remove_scale = QtWidgets.QPushButton(self.page_scale)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_remove_scale.setFont(font)
        self.btn_remove_scale.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(62, 63, 70, 0.7);\n"
"    min-width: 80px;\n"
"    image: url(UI/icons/remove.svg);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid rgba(217, 217, 217, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(217, 217, 217, 0.7);\n"
"    min-width: 80px;\n"
"    image: url(UI/icons/remove.svg);\n"
"}\n"
"\n"
"\n"
"")
        self.btn_remove_scale.setText("")
        self.btn_remove_scale.setIcon(icon3)
        self.btn_remove_scale.setIconSize(QtCore.QSize(25, 25))
        self.btn_remove_scale.setCheckable(True)
        self.btn_remove_scale.setChecked(False)
        self.btn_remove_scale.setObjectName("btn_remove_scale")
        self.verticalLayout_8.addWidget(self.btn_remove_scale)
        self.stackedWidget_size.addWidget(self.page_scale)
        self.verticalLayout_3.addWidget(self.stackedWidget_size, 0, QtCore.Qt.AlignBottom)
        self.gridLayout_3.addWidget(self.frame_2, 2, 2, 1, 1, QtCore.Qt.AlignRight)
        self.frame_3 = QtWidgets.QFrame(self.page_map)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(10, 10, 26, 0)
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget_turn = QtWidgets.QStackedWidget(self.frame_3)
        self.stackedWidget_turn.setObjectName("stackedWidget_turn")
        self.page_turn_invis = QtWidgets.QWidget()
        self.page_turn_invis.setObjectName("page_turn_invis")
        self.stackedWidget_turn.addWidget(self.page_turn_invis)
        self.page_turn_vis = QtWidgets.QWidget()
        self.page_turn_vis.setObjectName("page_turn_vis")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_turn_vis)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.btn_left = QtWidgets.QPushButton(self.page_turn_vis)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_left.setFont(font)
        self.btn_left.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(62, 63, 70, 0.7);\n"
"    min-width: 80px;\n"
"    image: url(UI/icons/rotate_left.svg);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid rgba(217, 217, 217, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(217, 217, 217, 0.7);\n"
"    min-width: 80px;\n"
"    image: url(UI/icons/rotate_left.svg);\n"
"}\n"
"\n"
"\n"
"")
        self.btn_left.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/rotate_left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_left.setIcon(icon4)
        self.btn_left.setIconSize(QtCore.QSize(25, 25))
        self.btn_left.setCheckable(True)
        self.btn_left.setChecked(False)
        self.btn_left.setObjectName("btn_left")
        self.verticalLayout_10.addWidget(self.btn_left)
        spacerItem4 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem4)
        self.btn_right = QtWidgets.QPushButton(self.page_turn_vis)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_right.setFont(font)
        self.btn_right.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(62, 63, 70, 0.7);\n"
"    min-width: 80px;\n"
"    image: url(UI/icons/rotate_right.svg);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid rgba(217, 217, 217, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(217, 217, 217, 0.7);\n"
"    min-width: 80px;\n"
"    image: url(UI/icons/rotate_right.svg);\n"
"}\n"
"\n"
"\n"
"")
        self.btn_right.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/rotate_right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_right.setIcon(icon5)
        self.btn_right.setIconSize(QtCore.QSize(25, 25))
        self.btn_right.setCheckable(True)
        self.btn_right.setChecked(False)
        self.btn_right.setObjectName("btn_right")
        self.verticalLayout_10.addWidget(self.btn_right)
        self.stackedWidget_turn.addWidget(self.page_turn_vis)
        self.page_size_text = QtWidgets.QWidget()
        self.page_size_text.setObjectName("page_size_text")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.page_size_text)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label = QtWidgets.QLabel(self.page_size_text)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_14.addWidget(self.label)
        self.stackedWidget_turn.addWidget(self.page_size_text)
        self.verticalLayout_4.addWidget(self.stackedWidget_turn)
        self.gridLayout_3.addWidget(self.frame_3, 2, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem5, 0, 1, 1, 1)
        self.stackedWidget_main.addWidget(self.page_map)
        self.verticalLayout_2.addWidget(self.stackedWidget_main)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget_btn.setCurrentIndex(1)
        self.stackedWidget_main.setCurrentIndex(0)
        self.stackedWidget_size.setCurrentIndex(0)
        self.stackedWidget_turn.setCurrentIndex(0)
        self.btn_camera.clicked.connect(self.btn_map.toggle) # type: ignore
        self.btn_map.clicked.connect(self.btn_camera.toggle) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Платформа"))
        self.btn_camera.setText(_translate("MainWindow", "Камера"))
        self.btn_map.setText(_translate("MainWindow", "Карта"))
        self.btn_settings.setItemText(0, _translate("MainWindow", "Загрузить"))
        self.btn_settings.setItemText(1, _translate("MainWindow", "Сохранить"))
        self.btn_settings.setItemText(2, _translate("MainWindow", "Отчистить"))
        self.btn_settings.setItemText(3, _translate("MainWindow", "Разместить платформу"))
        self.btn_settings.setItemText(4, _translate("MainWindow", "Добавить препятствие"))
        self.btn_settings.setItemText(5, _translate("MainWindow", "Нарисовать траекторию"))
        self.btn_settings.setItemText(6, _translate("MainWindow", "Изменить масштаб"))
        self.label.setText(_translate("MainWindow", "M 1:1"))
from Widget_settings.map_paint import Paint
