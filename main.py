# -*- coding: utf-8 -*-

import os, sys, struct
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *
from ui.MainWindow import Ui_MainWindow

class CITS(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(CITS,self).__init__()
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)

    window = CITS()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()