
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

class Parity:
    PARITY_NAMES = ['奇','偶','无']
    PARITYS = [QSerialPort.OddParity, QSerialPort.EvenParity, QSerialPort.NoParity]
    @staticmethod
    def getParity(i):
        return Parity.PARITYS[i]

class ByteSize:
    BYTESIZE_NAMES = ['5','6','7','8']
    BYTESIZES = [QSerialPort.Data5, QSerialPort.Data6, QSerialPort.Data7, QSerialPort.Data8]
    @staticmethod
    def getByteSize(i):
        return ByteSize.BYTESIZES[i]

class StopBits:
    STOPBITS_NAMES = ['1','2']
    STOPBITS = [QSerialPort.OneStop,QSerialPort.TwoStop]
    @staticmethod
    def getStopBits(i):
        return StopBits.STOPBITS[i]

class Baudrate:
    BAUDRATES = ['600','1200','2400','4800','9600','14400','19200','38400','57600','115200']
    @staticmethod
    def getBaudrate(i):
        return int(Baudrate.BAUDRATES[i])
