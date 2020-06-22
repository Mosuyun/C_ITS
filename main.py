# -*- coding: utf-8 -*-

import os, sys, struct
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *
from PyQt5.QtMultimedia import *
from ui.MainWindow import Ui_MainWindow

class CITS(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(CITS,self).__init__()
        self.setupUi(self)
        self.slot_connect()

    def slot_connect(self):
        self.openFile.triggered.connect(self.action_open_triggered)

    def action_open_triggered(self):
        fullpath, format = QFileDialog.getOpenFileName(self, '打开数据', '', 'video(*.mp4 *.avi)')
        print(fullpath)
        if os.path.exists(fullpath):
           self.loadVideo(fullpath)

    def loadVideo(self,fullpath):
        '''self.playlist=QMediaPlaylist()
        self.playlist.addMedia(QUrl.fromLocalFile(fullpath))
        self.playlist.setCurrentIndex(0)'''
        self.playerOrg.setVideoOutput(self.videoOrg)
        self.playerOrg.setMedia(QMediaContent(QUrl.fromLocalFile(fullpath)))
        #self.mplayer.setPlaylist(self.playlist)
        print(self.playerOrg.media())
        self.playerOrg.play()

        '''
        #向ui中添加videoWidgt
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
        '''



def main():
    app = QApplication(sys.argv)

    window = CITS()
    window.show()

    sys.exit(app.exec_())



if __name__ == '__main__':
    main()


