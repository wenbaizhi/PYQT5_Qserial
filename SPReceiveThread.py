import time
from PyQt5 import QtCore

class ReceiveThread(QtCore.QThread):
    # 接收到数据的信号槽

    received = QtCore.pyqtSignal(str)

    # 发生错误的信号槽
    error = QtCore.pyqtSignal(str)
    __ReceiveSate = False
    __flag = False

    def __init__(self, SpCore, QSerialPort, parent=None):  #传递参数
        super(ReceiveThread, self).__init__(parent)
        self.__spCore = SpCore         #对象
        self.__serialPort = QSerialPort  #新建对象
        self.__dataBuffer = b""
        # print(self.__serialPort)


    def stop(self):
        self.__flag = False
    def setReceiveStae(self):
        self.__ReceiveSate=True
        return self.__ReceiveSate

    # 设置是否以字符串接收
    def setReceiveString(self, e):

        self.__isReceiveString = e
        data = self.__decodeData(self.__dataBuffer)
        self.received.emit(data)

    # 获取接收缓冲区长度
    def getReceivedLength(self):
        return len(bytes(self.__dataBuffer))

    # 清空接收缓冲区
    def clearReceiveBuffer(self):
        self.__dataBuffer = b""
        data = self.__decodeData(self.__dataBuffer)
        self.received.emit(data)

    def __decodeData(self, rawData):
        data = ""
        if self.__isReceiveString:
            # 尝试以 gbk编码集 解码，如果失败再用 iso-8859-1编码集 解码
            try:
                data = rawData.decode("utf-8")
            except UnicodeDecodeError:
                data = rawData.decode("iso-8859-1")
        else:
            data = self.__spCore.dataArrayToString([self.__spCore.byteToHexString(x) for x in bytes(rawData)])

        return data

    def run(self):
        self.__flag = True
        self.__flag2 =False
        while self.__flag:

            if self.__serialPort.isOpen():

                try:
                    if self.__serialPort.bytesAvailable()> 0:

                        rawData = self.__serialPort.read(self.__serialPort.bytesAvailable())
                        # print(rawData)
                        self.__dataBuffer += rawData
                        data = self.__decodeData(self.__dataBuffer)
                        self.received.emit(data)
                except:
                    pass
                time.sleep(0.0001)
            else:
                time.sleep(0.5)
