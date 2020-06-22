# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1320, 765)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 10, 12)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.detection_out = QtWidgets.QLineEdit(self.centralwidget)
        self.detection_out.setObjectName("detection_out")
        self.verticalLayout.addWidget(self.detection_out, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(12, -1, 12, -1)
        self.horizontalLayout_3.setSpacing(24)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.videoLayout_org = QtWidgets.QHBoxLayout()
        self.videoLayout_org.setObjectName("videoLayout_org")
        self.horizontalLayout_3.addLayout(self.videoLayout_org)
        self.videoLayout_out = QtWidgets.QHBoxLayout()
        self.videoLayout_out.setSpacing(12)
        self.videoLayout_out.setObjectName("videoLayout_out")
        self.horizontalLayout_3.addLayout(self.videoLayout_out)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setObjectName("start")
        self.verticalLayout_2.addWidget(self.start)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.plateNumbers = QtWidgets.QTextEdit(self.centralwidget)
        self.plateNumbers.setObjectName("plateNumbers")
        self.verticalLayout_2.addWidget(self.plateNumbers)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 12)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.setStretch(0, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1320, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.openFile = QtWidgets.QAction(MainWindow)
        self.openFile.setObjectName("openFile")
        self.menu.addSeparator()
        self.menu.addAction(self.openFile)
        self.menubar.addAction(self.menu.menuAction())
        # 播放器初始化
        self.playerOrg = QMediaPlayer(self)
        self.playerOut = QMediaPlayer(self)
        # mVideoWidget控件初始化
        self.videoOrg = QVideoWidget(self)
        self.videoOut = QVideoWidget(self)
        # videoWidget添加进布局
        self.videoLayout_org.addWidget(self.videoOrg)
        self.videoLayout_out.addWidget(self.videoOut)
        # nplayer设置视频输出窗体（QVideoWideget）
        self.playerOrg.setVideoOutput(self.videoOrg)
        self.playerOut.setVideoOutput(self.videoOut)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start.setText(_translate("MainWindow", "开始检测"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">车牌号</p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.openFile.setText(_translate("MainWindow", "打开"))
