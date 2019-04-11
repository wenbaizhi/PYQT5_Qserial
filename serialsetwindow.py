from PyQt5.QtWidgets import QWidget
from SeralSetting import Ui_SerailSet
class SerailSet(QWidget,Ui_SerailSet):
    def __init__(self):
        super(SerailSet, self).__init__()
        self.setupUi(self)
        pass
    # def showchildwwindow(self,sys):
    #     self.__PortSetUI.show()
    #     pass