import time
from PyQt5 import QtCore
class SendCmd(QtCore.QThread):
    def __init__(self):
        pass

class A(object):
    def go(self):
        print ("go A go!")
    def stop(self):
        print ("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")
class B(A):
    def go(self):
        super(B, self).go()
        print ("go B go!B类实例化")
class C(A):
    def go(self):
        super(C, self).go()
        print ("go C go!C类实例化")
    def stop(self):
        super(C, self).stop()
        print ("stop C stop!")
class D(C,B):
    def go(self):
        super(D, self).go()
        print ("go D go!D类实例化")
    def stop(self):
        super(D, self).stop()
        print ("stop D stop!")
    def pause(self):
        print ("wait D wait!")
class E(B,C):
    pass
a = A()
b = B()
c = C()
d = D()
e = E()
# 说明下列代码的输出结果
a.go()
print('--------')
b.go()
print('--------')
c.go()
print('--------')
d.go()
print('--------')
e.go()
print('--------')
# a.stop()
# print('--------')
# b.stop()
# print('--------')
# c.stop()
# print('--------')
# d.stop()
# print('--------')
# e.stop()
print(D.mro())
# a.pause()
# b.pause()
# c.pause()
# d.pause()
# e.pause()