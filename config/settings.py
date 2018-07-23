import  os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal,QTimer
from config.untitled import Ui_MainWindow
from scr.Plot_branch import Prologue

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
    _signal = pyqtSignal(str)
    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "游戏界面第一次测试"))
        self.pushButton.setText(_translate("MainWindow", "发送"))
        self.pushButton_2.setText(_translate("MainWindow", "关闭"))
        #self._signal.connect(self.myPrint)
        self.textBrowser.setStyleSheet("color:red")
        self.textBrowser.setFont(QtGui.QFont("Microsoft YaHei", 28))
        self.pushButton.clicked.connect(self.auto_Print)

        self.pushButton_2.clicked.connect(QtCore.QCoreApplication.quit)



        #设置一个计时器
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.auto_Print)
        # self.timer.start(2000)
        self.list_Text = Prologue()
        #self.auto_Print
    def auto_Print(self):
        try:
            list_Text = next(self.list_Text)
            #text = "关于文本输出界面第四次尝试!!!!!!!!!!\n" + text
            self.textBrowser.setText(list_Text)
        except Exception as e:
            self.pushButton.clicked.connect(self.myPrint)

        #此处为文本框的接口,后续需要完善,,需要设定格式为水平靠右对齐
    def myPrint(self):
        self.textBrowser.append("也是关于文本输出界面的第四次尝试!\n")


