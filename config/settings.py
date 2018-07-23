import  os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from config.untitled import Ui_MainWindow

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class Setting(object):
    # 设置文件的说明
    def __init__(self):
        '''
        游戏的初始化设置
        '''
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
class Ui_New(Ui_MainWindow):
    '''
    关于这个类的说明,存储的都是一些,主要参数,其实可以另外新建一个跟ui代码完全没关系的方法的,正在尝试中/....
    '''
   # _signal = pyqtSignal(str)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "游戏界面第一次测试"))
        self.pushButton.setText(_translate("MainWindow", "发送"))
        self.pushButton_2.setText(_translate("MainWindow", "关闭"))

        self.pushButton.clicked.connect(self.myPrint)
        self.textBrowser.setText("关于文本输出界面第四次尝试!!!!!!!!!!\n")
        self.pushButton_2.clicked.connect(QtCore.QCoreApplication.quit)

        #self._signal.connect(self.mySignal)

        #此处为文本框的接口,后续需要完善

    def myPrint(self):
        self.textBrowser.append("也是关于文本输出界面的第四次尝试!\n")
        #self._signal.emit("第五次,第五次!!")

    # def mySignal(self, text):
    #     print(text)
    #     self.textBrowser.append("关于文本输出界面的第五次尝试", text)

# app = QtWidgets.QApplication(sys.argv)
# form = Ui_New()
# #form.find.connect(find)
# #form.replace.connect(replace)
# form.show()
# app.exec_()