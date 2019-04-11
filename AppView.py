# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
# from AppUi import Ui_MainWindow
from UISerial import Ui_MainWindow
from SeralSetting import Ui_SerailSet
from serialsetwindow import SerailSet
import sys
class ViewController(object):

    def __init__(self, window): #实例化 对象
        self.__window = window   #传递的为ViewController对象本身的实例 ，ViewController又继承自object 类
        # print(window)
        self.__ui = Ui_MainWindow()   #控件父类

        # self.__PortSetUI = Ui_SerailSet()
        self.PortSetUI= SerailSet() #子窗口
        self.__ui.setupUi(window)


        # self.__PortSetUI.setupUi(QObject)
        # self.__PortSetUI.selectPort.addItems(111)
        # self.setupUi(self, QObject)

        # self.__PortSetUI.setupUi()
        #self.__ui.editSendData.setFocus()

    # 初始化串口选项内容列表，实例化方法
    #  Python的参数传递既不是传值（pass-by-value），也不是传引用(pass-by-reference)，而是对象的引用（pass-by-object-reference），即传递的是一个对象的内存地址
    # 传递的参数均是对象
    def initComboBox(self, serialPort):  # 传递一个串口实例化对象
        pass
        # self.UIPortSet.selectPort.addItems(serialPort.getAvailablePortNames())
        self.PortSetUI.selectPort.addItems(serialPort.getAvailablePortNames())
        self.PortSetUI.selectBaudrate.addItems(serialPort.getBaudrateNames())
        self.PortSetUI.selectByteSize.addItems(serialPort.getByteSizeNames())
        self.PortSetUI.selectStopBits.addItems(serialPort.getStopBitsNames())
        self.PortSetUI.selectParity.addItems(serialPort.getParityNames())
        self.__ui.checkStringSend.setChecked(False)  #16进制 发送
        self.initSelections() #设置一个初始化串口


    # 更新可用串口选项列表
    def refreshAvailablePort(self, ports):
        pass

        # self.__PortSetUI.selectPort.clear()
        # self.__PortSetUI.selectPort.addItems(ports)
        # self.__PortSetUI.selectPort.update()


    # 初始化串口选项
    def initSelections(self):

        self.PortSetUI.selectPort.setCurrentIndex(0)
        self.PortSetUI.selectBaudrate.setCurrentIndex(4)
        self.PortSetUI.selectParity.setCurrentIndex(1)
        self.PortSetUI.selectByteSize.setCurrentIndex(3)
        self.PortSetUI.selectStopBits.setCurrentIndex(0)

    # 事件绑定
    def bindEvents(self, handler):
        self.PortSetUI.OpenCloseButton.setCheckable(True)
        self.__ui.SerialSetButton.clicked.connect(self.OpenserialsetUI)
        self.PortSetUI.OpenCloseButton.toggled.connect(handler.selectPorts)
        # self.__PortSetUI.OpenCloseButton.clicked.connect(handler.selectPorts)
        # self.__PortSetUI.OpenCloseButton.clicked.connect(self.)
        # self.__ui.editSendData.textChanged.connect(handler.inputSendData)
        # self.__ui.btnOpenClose.clicked.connect(handler.clickOpenClose)

        # self.__PortSetUI.selectPort.currentIndexChanged.connect(handler.selectPort)
        # self.UIPortSet.selectBaudrate.currentIndexChanged.connect(handler.selectBaudrate)
        # self.__ui.selectParity.currentIndexChanged.connect(handler.selectParity)
        # self.__ui.selectByteSize.currentIndexChanged.connect(handler.selectByteSize)
        # self.__ui.selectStopBits.currentIndexChanged.connect(handler.selectStopBits)
        self.__ui.checkStringSend.stateChanged.connect(handler.checkStringSend)
        # self.__ui.checkStringReceive.stateChanged.connect(handler.checkStringReceive)
        self.__ui.btnClearReceive.clicked.connect(handler.clickClearReceive)
        self.__ui.BtnSend.clicked.connect(handler.clickSend)

        # self.__ui.btnAutoSend.clicked.connect(handler.clickAutoSend)
       # self.__ui.btnScanPort.clicked.connect(handler.clickScanPort)

        # self.__ui.editCmd1.returnPressed.connect(lambda: handler.clickSendCmd(1))
        # self.__ui.editCmd2.returnPressed.connect(lambda: handler.clickSendCmd(2))
        # self.__ui.editCmd3.returnPressed.connect(lambda: handler.clickSendCmd(3))
        # self.__ui.editCmd4.returnPressed.connect(lambda: handler.clickSendCmd(4))
        # self.__ui.editCmd5.returnPressed.connect(lambda: handler.clickSendCmd(5))
        # self.__ui.editCmd6.returnPressed.connect(lambda: handler.clickSendCmd(6))
        # self.__ui.editCmd7.returnPressed.connect(lambda: handler.clickSendCmd(7))
        # self.__ui.editCmd8.returnPressed.connect(lambda: handler.clickSendCmd(8))
        # self.__ui.editCmd9.returnPressed.connect(lambda: handler.clickSendCmd(9))
        # self.__ui.editCmd10.returnPressed.connect(lambda: handler.clickSendCmd(10))
        # self.__ui.btnSendCmd1.clicked.connect(lambda: handler.clickSendCmd(1))
        # self.__ui.btnSendCmd2.clicked.connect(lambda: handler.clickSendCmd(2))
        # self.__ui.btnSendCmd3.clicked.connect(lambda: handler.clickSendCmd(3))
        # self.__ui.btnSendCmd4.clicked.connect(lambda: handler.clickSendCmd(4))
        # self.__ui.btnSendCmd5.clicked.connect(lambda: handler.clickSendCmd(5))
        # self.__ui.btnSendCmd6.clicked.connect(lambda: handler.clickSendCmd(6))
        # self.__ui.btnSendCmd7.clicked.connect(lambda: handler.clickSendCmd(7))
        # self.__ui.btnSendCmd8.clicked.connect(lambda: handler.clickSendCmd(8))
        # self.__ui.btnSendCmd9.clicked.connect(lambda: handler.clickSendCmd(9))
        # self.__ui.btnSendCmd10.clicked.connect(lambda: handler.clickSendCmd(10))

    # 更新串口打开/关闭状态
    def openOrCloseSerialPort(self, e):
        self.__ui.btnOpenClose.setText("打开串口" if not e else "关闭串口")

    # 更新串口打开/关闭状态
    def startOrEndAutoSend(self, e):
        self.__ui.btnAutoSend.setText("开始自动发送" if not e else "停止自动发送")
        self.__ui.editSendData.setEnabled(not e)
        self.__ui.editInterval.setEnabled(not e)

    # 根据 objectName 设置 QComboBox 当前选择项
    def setSelectedIndex(self, objectName, i):
        return self.__window.findChild(QtWidgets.QComboBox, objectName).setCurrentIndex(i)
    # 根据 objectName 设置 QComboBox 当前选择内容
    def setSelectedText(self, objectName, t):
        return self.__window.findChild(QtWidgets.QComboBox, objectName).setCurrentText(t)
    # 根据 objectName 获取 QComboBox 当前选择项
    def getSelectedIndex(self, objectName):
        return self.__window.findChild(QtWidgets.QComboBox, objectName).currentIndex()
    # 根据 objectName 获取 QComboBox 当前选择内容
    def getSelectedText(self, objectName):
        return self.__window.findChild(QtWidgets.QComboBox, objectName).currentText()

    # 根据 objectName 获取 QCheckBox 当前状态
    def getCheckedStatus(self, objectName):
        # print(self.__ui.checkStringSend.isChecked())
        return self.__ui.checkStringSend.isChecked()

    # 获取和设置接收数据内容
    def getReceivedText(self):
        # return self.__window.findChild(QtWidgets.QTextEdit, "editReceiveData").toPlainText()
        return self.__ui.RXtextEdit.toPlainText()

    def setReceivedText(self, text):
        self.__ui.RXtextEdit.setPlainText(text)
        self.__ui.RXtextEdit.moveCursor(QtGui.QTextCursor.End)
        # self.__window.findChild(QtWidgets.QTextEdit, "editReceiveData").setPlainText(text)
        # self.__window.findChild(QtWidgets.QTextEdit, "editReceiveData").moveCursor(QtGui.QTextCursor.End)

    # 清空接收数据
    def clearReceivedData(self):
        self.__ui.RXtextEdit.setText("")
        # self.__window.findChild(QtWidgets.QTextEdit, "editReceiveData").setText("")

    def setReceivedLength(self, l):
        self.__ui.receivedLength.setText(str(l))
        pass
        # self.__window.findChild(QtWidgets.QLabel, "receivedLength").setText(str(l))

    # 获取和设置发送数据内容
    def getSendText(self):
        print("读取数据")
        print( self.__ui.editSendData.text())  #获取lineEdit对象的内容
        return self.__ui.editSendData.text()
        # print( self.__ui.editSendData.toPlainText())#获取TextEdit对象的内容
        # return self.__ui.editSendData.toPlainText()
        # return self.__window.findChild(QtWidgets.QTextEdit, "editSendData").toPlainText()
    def setSendText(self, text):
        self.__ui.editSendData.setPlainText(text)
        # self.__window.findChild(QtWidgets.QTextEdit, "editSendData").setPlainText(text)
    # 获取和设置发送数据内容光标
    def getSendTextCursor(self):
        return self.__ui.editSendData.textCursor()
        # return self.__window.findChild(QtWidgets.QTextEdit, "editSendData").textCursor()
    def setSendTextCursor(self, cursor):
        # self.__window.findChild(QtWidgets.QTextEdit, "editSendData").setTextCursor(cursor)
        return self.__ui.editSendData.setTextCursor(cursor)
    # 获取十六进制命令数据内容
    def getCmdText(self, i):
        return self.__window.findChild(QtWidgets.QLineEdit, "editCmd" + str(i)).text()

    # 获取自动发送间隔内容
    def getAutoSendInterval(self):
        return self.__window.findChild(QtWidgets.QLineEdit, "editInterval").text()
    def OpenserialsetUI(self):
        self.PortSetUI.show()







# if __name__ == "__main__":
#     # 设置应用唯一的AppID
#     # appID = u'dennic.serialport.tool.v1.0'
#     # ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appID)
#     # 实例化应用
# 	app = QtWidgets.QApplication(sys.argv)
#     # 实例化主窗口
# 	mainWindow = MainWindow()
#     # 显示主窗口
# 	mainWindow.show()
#     # 应用执行结束后退出
# 	sys.exit(app.exec_())
