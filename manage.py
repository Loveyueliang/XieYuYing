#! /usr/bin/env python
# -*- coding: utf-8 -*-
import  os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from config import settings

#from bin.main import main

if __name__ == "__main__":
    #main()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = settings.Ui_New()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

"""
PlayPlane/
|-- bin/
|   |-- main.py         程序运行主体程序
|-- config/
|   |-- settings.py     程序配置(例如: 游戏背景音乐的加载等)
|-- material            程序素材放置(如配音,图片素材放置)
    |-- ...
|-- src/                程序主体模块存放
|   |-- __init__.py 
|   |-- character.py    所有角色类代码存放
|   |-- Test_Asset.py   对话类(主要是玩家)代码存放
|   |-- ...             后续所需的类文件
|-- manage.py           程序启动文件(现在写的是启动图形界面的代码)
|-- README.md           
"""