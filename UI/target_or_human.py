# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\target_or_human.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(384, 293)
        Dialog.setStyleSheet("background-color: rgb(147, 147, 147);\n"
"border: 2px solid rgba(62, 63, 70, 0);\n"
"border-radius: 6px;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_power = QtWidgets.QPushButton(Dialog)
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
"    image: url(UI/icons/cancel.svg);\n"
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
        self.btn_power.setCheckable(False)
        self.btn_power.setObjectName("btn_power")
        self.verticalLayout.addWidget(self.btn_power, 0, QtCore.Qt.AlignLeft)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 135))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_target = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_target.setFont(font)
        self.btn_target.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(62, 63, 70, 0.7);\n"
"    image: url(UI/icons/target.svg);\n"
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
        self.btn_target.setText("")
        self.btn_target.setIconSize(QtCore.QSize(25, 25))
        self.btn_target.setCheckable(True)
        self.btn_target.setObjectName("btn_target")
        self.horizontalLayout.addWidget(self.btn_target)
        self.btn_human = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_human.setFont(font)
        self.btn_human.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 6px;\n"
"    background-color: rgba(62, 63, 70, 0.7);\n"
"    image: url(UI/icons/emoji.svg);\n"
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
        self.btn_human.setText("")
        self.btn_human.setIconSize(QtCore.QSize(25, 25))
        self.btn_human.setCheckable(True)
        self.btn_human.setObjectName("btn_human")
        self.horizontalLayout.addWidget(self.btn_human)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        self.btn_power.clicked.connect(Dialog.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Выбор режима следования:"))