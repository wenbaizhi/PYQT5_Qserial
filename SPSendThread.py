import time
from PyQt5 import QtCore
from PyQt5.QtCore import QIODevice
import queue
from PyQt5.QtWidgets import QMessageBox
import binascii
class SendThread(QtCore.QThread,QMessageBox):
    # 自动发送的信号槽
    autoSendError = QtCore.pyqtSignal(str)
    # 发生错误的信号槽
    error = QtCore.pyqtSignal(str)
    tosend = QtCore.pyqtSignal(str)
    __flag = False
    __isAutoSend = False
    __isSendCmd=False

    def __init__(self, SpCore, QSerialPort ,parent=None):  # 传递参数
        super(SendThread, self).__init__(parent)
        self.__spCore = SpCore
        self.__serialPort = QSerialPort
        self.__sendQueue = queue.Queue()


        #self.__windowmain = windowmain
    def stop(self):
        self.__flag = False

    # 设置是否以字符串发送
    def setSendString(self, e):
        self.__isSendHex = e
        if self.__isSendHex:
            print("HEX码发送")
        else:
            print("字符串发送")

    # 开始自动发送
    def startAutoSend(self, data, interval):
        self.__autoSendData = data
        self.__autoSendInterval = interval
        self.__isAutoSend = True
    # 停止自动发送
    def stopAutoSend(self):
        self.__isAutoSend = False

    # 获取自动发送状态
    def isAutoSend(self):
        return self.__isAutoSend

    def sendCmdSP(self, data):
        self.__isSendCmd=True
        self.__autoSendData=data
        if data.isalnum:
            self.__isSendHex=False
        else:
            self.__isSendHex = True
            # self.setSendString(self, False)
        # print("待发数据是"+self.__autoSendData)
        # return True, "串口未打开！"
    # 发送数据， 添加到发送队列
    def sendData(self, data):
            try:
                if not self.__serialPort.isOpen():
                    # QMessageBox.critical(self, '错误', '转换编码错误')
                    return False, "串口未打开！"
                # print(self.__isSendString)
                if not self.__isSendHex:
                    dataBytes = data.encode('UTF-8')
                    print(dataBytes)
                    self.__serialPort.write(dataBytes)
                    # print(data)
                    print("字符发送成功")
                else:    #hex码发送
                    dataBytes = self.__spCore.hexStringToByteArray(data)
                    if not dataBytes:
                        return False, "请正确输入HEX格式数据，如“FF C0 A3”。"
                    self.__serialPort.write(bytes(dataBytes))
                    print(bytes(dataBytes))
                # self.__sendQueue.put(dataBytes)
                # print(dataBytes)


                return True, "发送成功！"
            except:
                return False, "发送失败！"



    def sendCmd1(self, data):
        try:
            if not self.__serialPort.isOpen():
                return False, "串口未打开！"
            if data.isalnum() is True:
                    dataBytes = self.__spCore.hexStringToByteArray(data)
                    if not dataBytes:
                        return False, "请正确输入HEX格式数据，如“FF C0 A3”。"
                # self.__sendQueue.put(dataBytes)
                # print(dataBytes)
                    self.__serialPort.write(bytes(dataBytes))
            else:
                dataBytes = data.encode('UTF-8')
                self.__serialPort.write(dataBytes)
            # if not dataBytes:
            #     return False, "请正确输入HEX格式数据，如“FF C0 A3”。"
            # self.__sendQueue.put(dataBytes)
            return True, "发送成功！"
        except:
            return False, "发送失败！"

    def run(self):
        self.__flag = True
        lastSendTime = 0
        while self.__flag:
            if self.__isSendCmd:
                self.__isSendCmd = False
                self.sendData(self.__autoSendData)
            # 自动发送
            # if self.__isAutoSend:
            #     nowTime = time.time()*1000
            #     if nowTime - lastSendTime >= self.__autoSendInterval:
            #         lastSendTime = nowTime
            #         success, msg = self.sendData(self.__autoSendData)
            #         if not success:
            #             self.stopAutoSend()
            #             self.autoSendError.emit(msg)

            if self.__serialPort.isOpen():
                 # if not self.__sendQueue.empty():
                 # #  self.__serialPort.waitForBytesWritten():
                    try:
                 #        print(self.__sendQueue.get())
                 #        self.__serialPort.writeData(([2,3,6]))

                         self.tosend.emit("123")
                    except:
                        pass
                    time.sleep(1)
            else:
                time.sleep(0.5)

