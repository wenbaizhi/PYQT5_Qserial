# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

import ctypes

# from AppIcon import AppIcon
from AppView import ViewController,SerailSet



from SerialPort import SPCore,SPReceiveThread
import EventHandler
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.serialPort = SPCore.SerialPort()  # 实例化类对象
        # self.setWindowIcon(AppIcon().getQIcon())
        self.view = ViewController(self)  #显示窗口实例化 ，init 方法内 参数window 传递的为实例本身
        # self.childView=SerailSet(self)
        self.handler = EventHandler.handler(self)
        # self.PortSetUI = SerailSet()
        self.view.bindEvents(self.handler)
        # self.serialPort.sendThread.autoSendError.connect(self.handler.autoSendError)
        self.serialPort.receiveThread.received.connect(self.handler.receivedData)
        self.serialPort.sendThread.tosend.connect(self.handler.tosendData)
        self.serialPort.sendThread.error.connect(self.handler.serialIOError)
        # self.serialPort.receiveThread.error.connect(self.handler.serialIOError)
        self.view.initComboBox(self.serialPort)

    # 调用串口类发送数据
    def sendDataUi(self):
        sendData = self.view.getSendText()
        # self.serialPort.sendThread.setSendString(sendData)
        success, msg = self.serialPort.sendThread.sendData(sendData)
        if not success:
            self.showWarning(msg)

    # 调用串口类发送十六进制命令
    def sendCmd(self, data):
        # pass
        # self.serialPort.sendThread.sendCmd(data)
        success, msg = self.serialPort.sendThread.sendCmdSP(data)
        if not success:
            print(msg)
            self.showWarning(msg)

    def showWarning(self, msg):
        pass
        messageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, " ", msg)
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Yes)
        # # messageBox.setWindowIcon(AppIcon().getQIcon())
        button = messageBox.button(QtWidgets.QMessageBox.Yes)
        button.setText('确认')
        messageBox.exec_()

    def closeEvent(self,event):
        pass
        self.serialPort.sendThread.stop()
        self.serialPort.receiveThread.stop()
        self.serialPort.close()
        event.accept()


# import sys
if __name__ == "__main__":

    # 设置应用唯一的AppID
    # appID = u'dennic.serialport.tool.v1.0'
    # ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appID)
    # 实例化应用
	app = QtWidgets.QApplication(sys.argv)
    # 实例化主窗口
	mainWindow = MainWindow()
    # 显示主窗口
	mainWindow.show()
    # 应用执行结束后退出
	sys.exit(app.exec_())
