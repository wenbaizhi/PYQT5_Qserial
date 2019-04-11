# -*- coding: utf-8 -*-
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from SerialPort import SPOptions, SPSendThread, SPReceiveThread
from PyQt5.QtWidgets import QMessageBox
import binascii
from PyQt5.QtCore import  QIODevice
class SerialPort(object):
    # __port = 'com1'
    # __baudrate = 9600
    # __parity=serial.PARITY_NONE
    # __stopbits=serial.STOPBITS_ONE
    # __bytesize=serial.EIGHTBITS

    # 是否以字符串发送/接收数据
    __sendHex = False   #类属性
    __receiveString = False
    __com_list = []     #串口序列
    def __init__(self):
        # 实例化串口类
        self.__serialPort = QSerialPort()
        # 实例化并启动发送/接收线程 类
        self.sendThread = SPSendThread.SendThread(self, self.__serialPort)
        self.receiveThread = SPReceiveThread.ReceiveThread(self, self.__serialPort)
        # # # 置发送和接收状态机
        self.receiveThread.setReceiveString(self.__receiveString)
        self.sendThread.setSendString(self.__sendHex)   #引用时如果类没有则会新建一个 ，如果有则引用类调用类属性

        # # # 启动线程
        # self.sendThread.start()
        self.receiveThread.start()

    def getAvailablePortNames(self):
        # pass
        resultPort = []
        __com_list = QSerialPortInfo.availablePorts()

        for info in __com_list:
            self.__serialPort.setPort(info)
            print(__com_list)
            if self.__serialPort.open(QSerialPort.ReadWrite):
                resultPort.append(info.portName())
                self.__serialPort.close()
                print(resultPort)
                # self.__serialPorte.setPortNam(0)

        return resultPort
    # 打开串口
    def openSp(self):
        if self.isOpen():
            self.close()
        try:
            if self.__serialPort.open(QSerialPort.ReadWrite) == False:
                QMessageBox.critical(self.__ui, '严重错误', '串口打开失败')
                return
        except:
            QMessageBox.critical(self, '严重错误', '串口打开失败')
            return
        # if self.isOpen():
        #     self.close()
        # try:
        #     # print(self.__serialPort.port)
        #     # print(self.__serialPort.baudrate)
        #     # print(self.__serialPort.bytesize)
        #     # print(self.__serialPort.parity)
        #     # print(self.__serialPort.stopbits)
        #     self.__serialPort.open()
        #     return True, "串口打开成功！"
        # except Exception as e:
        #     msg = "无法打开串口！"
        #     if str(e).find("PermissionError") >= 0:
        #         msg = "串口 {!r} 已被占用！".format(str(self.__serialPort.port).upper())
        #     return False , msg

    # 关闭串口
    def close(self):
        if self.isOpen():
            try:
                self.__serialPort.close()
                return True
            except:
                pass
        return False

    # 返回串口打开/关闭状态
    def isOpen(self):
        return self.__serialPort.isOpen()


    # 设置串口
    def setPortQt(self, port):
        # self.__serialPort.setPort(port)
        # self.__serialPort.setPortName(port.PortName)
        try:
            self.__serialPort.port = port
            return True, "串口打开成功！"
        except Exception as e:
            msg = "串口打开失败！"
            if str(e).find("PermissionError") >= 0:
                msg = "串口 {!r} 已被占用！".format(str(self.__serialPort.port).upper())
            return False, msg

    # 获取当前串口
    def getPort(self):
        return self.__serialPort.port

    # 设置波特率
    def setBaudrate(self, b):
        self.__serialPort.setBaudRate(b)

    # 设置校验位
    def setParity(self, p):
        self.__serialPort.setParity(p)

    # 设置数据位
    def setByteSize(self, b):
        self.__serialPort.setDataBits( b)

    # 设置停止位
    def setStopBits(self, s):
        self.__serialPort.setStopBits(s)

    # 设置发送字符串数据
    def setSendString(self,e):
        self.__sendHex = e
        self.sendThread.setSendString(e)


    #
    # 设置接收字符串数据
    def setReceiveString(self,e):
        self.__receiveString = e
        self.receiveThread.setReceiveString(e)

    # 获取可选 COM 口名称


    def getAvailablePortlist(self):
        return self.__com_list

        # result = []
        # coms = ['COM%s' % i for i in range(1,257)]
        # for port in coms:
        #     try:
        #         s = __serialPort.Serial(port)
        #         s.close()
        #         result.append(port)
        #     except __serialPort.SerialException as e:
        #         if str(e).find("PermissionError") >= 0:
        #             result.append(port)
        # if len(result) == 0:
        #     result.append("(无可用)")
        # return result
    #
    def setSpName(self,a):
        self.__serialPort.setPortName(a)
    # 获取可选波特率名称
    def getBaudrateNames(self):
        return SPOptions.Baudrate.BAUDRATES

    # 获取可选校验位名称
    def getParityNames(self):
        return SPOptions.Parity.PARITY_NAMES

    # 获取可选数据位名称
    def getByteSizeNames(self):
        return SPOptions.ByteSize.BYTESIZE_NAMES

    # 获取可选停止位名称
    def getStopBitsNames(self):
        return SPOptions.StopBits.STOPBITS_NAMES

    # 数据数组转可读字符串
    def dataArrayToString(self,l):
    	s = ""
    	for i in l:
    		s += (str(i)+" ")
    	return s

    # 字节转十六进制字符串
    def byteToHexString(self,b):
    	h = hex(b)
    	h = h.replace("0x","")
    	if len(h) == 1:
    		h = "0" + h
    	return h.upper()

    # 十六进制字符串转字节数组
    def hexStringToByteArray(self, s):
        try:
            data = s.split()
            hexData = []
            for b in data:
                hexData.append(int(b, 16))
            print(hexData)
            #dataBytes = bytes(hexData)

            return hexData
        except:
            return None
