# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SeralSetting.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SerailSet(object):
    def setupUi(self, SerailSet):
        SerailSet.setObjectName("SerailSet")
        SerailSet.resize(489, 264)
        self.OpenCloseButton = QtWidgets.QPushButton(SerailSet)
        self.OpenCloseButton.setGeometry(QtCore.QRect(350, 70, 101, 61))
        self.OpenCloseButton.setObjectName("OpenCloseButton")
        self.label_9 = QtWidgets.QLabel(SerailSet)
        self.label_9.setGeometry(QtCore.QRect(20, 30, 108, 20))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(SerailSet)
        self.label_11.setGeometry(QtCore.QRect(0, 110, 107, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(SerailSet)
        self.label_12.setGeometry(QtCore.QRect(0, 150, 107, 20))
        self.label_12.setObjectName("label_12")
        self.selectParity = QtWidgets.QComboBox(SerailSet)
        self.selectParity.setGeometry(QtCore.QRect(120, 110, 141, 20))
        self.selectParity.setObjectName("selectParity")
        self.selectStopBits = QtWidgets.QComboBox(SerailSet)
        self.selectStopBits.setGeometry(QtCore.QRect(120, 150, 141, 20))
        self.selectStopBits.setObjectName("selectStopBits")
        self.selectBaudrate = QtWidgets.QComboBox(SerailSet)
        self.selectBaudrate.setGeometry(QtCore.QRect(120, 70, 141, 20))
        self.selectBaudrate.setObjectName("selectBaudrate")
        self.label_10 = QtWidgets.QLabel(SerailSet)
        self.label_10.setGeometry(QtCore.QRect(30, 60, 81, 31))
        self.label_10.setObjectName("label_10")
        self.selectPort = QtWidgets.QComboBox(SerailSet)
        self.selectPort.setGeometry(QtCore.QRect(120, 30, 141, 22))
        self.selectPort.setObjectName("selectPort")
        self.selectByteSize = QtWidgets.QComboBox(SerailSet)
        self.selectByteSize.setGeometry(QtCore.QRect(120, 180, 141, 20))
        self.selectByteSize.setObjectName("selectByteSize")
        self.label_13 = QtWidgets.QLabel(SerailSet)
        self.label_13.setGeometry(QtCore.QRect(0, 180, 107, 20))
        self.label_13.setObjectName("label_13")

        self.retranslateUi(SerailSet)
        QtCore.QMetaObject.connectSlotsByName(SerailSet)

    def retranslateUi(self, SerailSet):
        _translate = QtCore.QCoreApplication.translate
        SerailSet.setWindowTitle(_translate("SerailSet", "通信设置"))
        self.OpenCloseButton.setText(_translate("SerailSet", "打开串口"))
        self.label_9.setText(_translate("SerailSet", "     串口号"))
        self.label_11.setText(_translate("SerailSet", "        校验位"))
        self.label_12.setText(_translate("SerailSet", "        停止位"))
        self.label_10.setText(_translate("SerailSet", "   波特率"))
        self.label_13.setText(_translate("SerailSet", "        数据位"))

