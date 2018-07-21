import  os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from config import untitled

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = untitled.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())