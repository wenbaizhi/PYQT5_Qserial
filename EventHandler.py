# -*- coding: utf-8 -*-
from SerialPort import SPOptions
from serialsetwindow import SerailSet
import sys
import EventHandler
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
class handler(object):
    def __init__(self,window):
        self.__window = window
        # self.__serialPorts=[]
        # self.a=0
        # self.isopen = False
        pass
    # def test(self):
    #     print("11111")
    # def OpenserialsetUI(self):
    #     self.UI_Serial.show()

        # self
    #
    # # 点击开启/关闭串口按钮
    # def clickOpenClose(self, event=None):
    #     if not self.__window.serialPort.isOpen():
    #         success, msg = self.__window.serialPort.open()
    #         if success:
    #             # 更新界面显示 已开启串口
    #             self.__window.view.openOrCloseSerialPort(True)
    #         else:
    #             self.__window.showWarning(msg)
    #     else:
    #         self.__window.serialPort.close()
    #         # 更新界面显示 已关闭串口
    #         self.__window.view.openOrCloseSerialPort(False)
    #
    # # 点击扫描可用串口按钮
    # def clickScanPort(self, event=None):
    #     self.__window.serialPort.close()
    #     self.__window.view.openOrCloseSerialPort(False)
    #     self.__window.view.refreshAvailablePort(self.__window.serialPort.getAvailablePortNames())
    #
    #选择串口
    # def selectPorts(self, event=None):
    #     print("set uart")
    #     self.__window.serialPort.setStopBits(SPOptions.StopBits.getStopBits(self.__window.view.getSelectedIndex("selectStopBits")))
        # pass
        # self.a= SPOptions.Baudrate.getBaudrate(self.__window.view.PortSetUI.getSelectedIndex("selectBaudrate"))
        # print(self.a)
    def selectPorts(self, event=None):

        if self.__window.view.PortSetUI.OpenCloseButton.isChecked():
            # self.__serialChennel = QSerialPortInfo.availablePorts()
            # self.__serialChennel=self.__window.serialPort.getAvailablePortlist()
            # print(self.__serialChennel)

            # print(self.__serialChennel.portName)
            # self.__window.serialPort.setPortQt(self.__serialChennel)
            # self.__window.serialPort.setPortQt(self.__serialChennel[self.__window.view.PortSetUI.selectPort.currentIndex()])
            self.__window.serialPort.setSpName(self.__window.view.PortSetUI.selectPort.currentText())
            print(self.__window.view.PortSetUI.selectPort.currentText())
            self.__window.serialPort.openSp()
            # print(str(self.__window.view.PortSetUI.selectPort.currentText()))
            self.__window.serialPort.setBaudrate(SPOptions.Baudrate.getBaudrate(self.__window.view.PortSetUI.selectBaudrate.currentIndex()))
            self.__window.serialPort.setParity(SPOptions.Parity.getParity(self.__window.view.PortSetUI.selectParity.currentIndex()))
            self.__window.serialPort.setByteSize(SPOptions.ByteSize.getByteSize(self.__window.view.PortSetUI.selectByteSize.currentIndex()))
            self.__window.serialPort.setStopBits(SPOptions.StopBits.getStopBits(self.__window.view.PortSetUI.selectStopBits.currentIndex()))


            self.__window.view.PortSetUI.selectBaudrate.setDisabled(True)
            self.__window.view.PortSetUI.selectParity.setDisabled(True)
            self.__window.view.PortSetUI.selectByteSize.setDisabled(True)
            self.__window.view.PortSetUI.selectStopBits.setDisabled(True)
            self.__window.view.PortSetUI.selectPort.setDisabled(True)
            self.__window.view.PortSetUI.OpenCloseButton.setText("关闭串口")
            print("串口初始化 完成")
        else:
            self.__window.view.PortSetUI.OpenCloseButton.setText("打开串口")
            self.__window.view.PortSetUI.selectBaudrate.setEnabled(True)
            self.__window.view.PortSetUI.selectParity.setEnabled(True)
            self.__window.view.PortSetUI.selectByteSize.setEnabled(True)
            self.__window.view.PortSetUI.selectStopBits.setEnabled(True)
            self.__window.view.PortSetUI.selectPort.setEnabled(True)
            self.__window.serialPort.close()
            print("关闭串口")

        # pass
        # self.__window.serialPort.setBaudrate(SPOptions.Baudrate.getBaudrate(self.__window.view.getSelectedIndex("selectBaudrate")))
        # print("set uart")
        #self.__window.view.PortSetUI.getSelectedIndex("selectBaudrate")
        # self.__window.serialPort.setPort(self.__window.UIPortSet.)
        # self.__window.serialPort.setPort(self.UIPortSet)
        # success, msg = self.UIPortSet.serialPort.setPort(self.__window.view.getSelectedText("selectPort"))
        # if not success and not self.__window.serialPort.isOpen():
        #     self.__window.view.openOrCloseSerialPort(False)
        #     self.__window.showWarning(msg)
    # # 选择波特率
    # def selectBaudrate(self, event=None):
    #     self.__window.serialPort.setBaudrate(SPOptions.Baudrate.getBaudrate(self.__window.view.getSelectedIndex("selectBaudrate")))
    # # 选择校验位
    # def selectParity(self, event=None):
    #     self.__window.serialPort.setParity(SPOptions.Parity.getParity(self.__window.view.getSelectedIndex("selectParity")))
    # 选择数据位
    # def selectByteSize(self, event=None):
    #     self.__window.serialPort.setByteSize(SPOptions.ByteSize.getByteSize(self.__window.view.getSelectedIndex("selectByteSize")))
    # # 选择停止位
    # def selectStopBits(self, event=None):
    #     self.__window.serialPort.setStopBits(SPOptions.StopBits.getStopBits(self.__window.view.getSelectedIndex("selectStopBits")))
    # # 发送字符串数据
    def checkStringSend(self, event=None):
        self.__window.serialPort.setSendString(self.__window.view.getCheckedStatus("checkStringSend"))
    # # 接收字符串数据
    # def checkStringReceive(self, event=None):
    #     self.__window.serialPort.setReceiveString(self.__window.view.getCheckedStatus("checkStringReceive"))
    #r
    # # 点击清空接收数据
    def clickClearReceive(self, event=None):
        self.__window.serialPort.receiveThread.clearReceiveBuffer()
        self.__window.view.setReceivedLength(self.__window.serialPort.receiveThread.getReceivedLength())

    # # 点击发送数据
    def clickSend(self, event=None):
        self.__window.sendDataUi()
    #
    # # 点击发送十六进制命令
    # def clickSendCmd(self, i, event=None):
    #     text = self.__window.view.getCmdText(i)
    #     self.__window.sendCmd(text)
    #
    # # 点击自动发送
    # def clickAutoSend(self, event=None):
    #     if self.__window.serialPort.sendThread.isAutoSend():
    #         self.__window.serialPort.sendThread.stopAutoSend()
    #         self.__window.view.startOrEndAutoSend(False)
    #     else:
    #         try:
    #             interval = int(self.__window.view.getAutoSendInterval())
    #             if interval < 10:
    #                 self.__window.showWarning("自动发送周期不能小于10毫秒！")
    #                 return
    #             sendData = self.__window.view.getSendText()
    #             self.__window.view.startOrEndAutoSend(True)
    #             self.__window.serialPort.sendThread.startAutoSend(sendData, interval)
    #         except:
    #             self.__window.showWarning("请正确输入自动发送周期！")
    #
    # # 自动发送错误
    # def autoSendError(self, msg):
    #     self.__window.view.startOrEndAutoSend(False)
    #     self.__window.showWarning(msg)
    #
    # 更新接收到的数据
    def receivedData(self, data):
        pass
        self.__window.view.setReceivedText(data)
        self.__window.view.setReceivedLength(self.__window.serialPort.receiveThread.getReceivedLength())
    #
    def serialIOError(self, msg="串口IO错误！"):
        self.__window.serialPort.close()
        # self.__window.view.openOrCloseSerialPort(False)
        self.__window.showWarning(msg)

    def tosendData(self,data):
        print(data)
        # print(self.serialPort.sendThread.sendCmdSP)
        self.__window.serialPort.sendThread.sendCmdSP(data)
        # self.serialPort.sendThread.sendCmdSP(data)
        # self.__window.sendCmd(self, data)
    #
    # 监听发送数据的输入，当输入回车时调用 window 的 sendData 方法
    def inputSendData(self, event=None):
        cursor = self.__window.view.getSendTextCursor()
        cursorPosition = cursor.position()
        text = self.__window.view.getSendText()
        # 当前输入位置字符为换行符时执行
        if cursorPosition > 0 and text[cursorPosition-1] == "\n":
            # 删除换行符
            self.__window.view.setSendText(self.__removeCharFromString(text,cursorPosition-1))
            cursor.setPosition(cursorPosition-1 if cursorPosition-1>0 else 0)
            self.__window.view.setSendTextCursor(cursor)
            # 调用 window 的 sendData 方法发送数据
            self.__window.sendData()
    #
    #
    # # 删除字符串中指定位置字符
    # # 参数 s : 原字符串
    # # 参数 p : 要删除的字符位置
    # # 返回 : 删除后的字符串
    # def __removeCharFromString(self,s,p):
    #     return s[0:p] + s[p+1:len(s)]
