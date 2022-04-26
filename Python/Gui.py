# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Prorest4.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
import sys
from plyer import notification
from Database import *
import pafy
import vlc
import random

class Ui_Prorest(QDialog):
    breakChoice = 1
    musicOrder = 1
    musicRandom = 1
    
    def setupUi(self, Prorest):
        Prorest.setObjectName("Prorest")
        Prorest.resize(806, 603)
        Prorest.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(151, 45, 219, 252), stop:1 rgba(72, 151, 183, 252));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(63, 134, 213, 227), stop:0.994737 rgba(194, 255, 135, 252));")
        self.centralwidget = QtWidgets.QWidget(Prorest)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 781, 541))
        self.tabWidget.setStyleSheet("font: 75 10pt \"Garamond\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(111, 39, 186, 241), stop:0.994737 rgba(170, 20, 119, 209));\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.break_bg = QtWidgets.QLabel(self.tab)
        self.break_bg.setGeometry(QtCore.QRect(-6, -25, 781, 571))
        self.break_bg.setText("")
        self.break_bg.setPixmap(QtGui.QPixmap("../Python/BG/ThinkstockPhotos-489763838-e1490767826261.jpg"))
        self.break_bg.setObjectName("break_bg")
        self.break_btn = QtWidgets.QPushButton(self.tab, clicked = lambda: self.break_press())
        self.break_btn.setGeometry(QtCore.QRect(290, 290, 191, 61))
        self.break_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 219, 182, 252), stop:1 rgba(209, 255, 137, 252));\n"
"font: 75 14pt \"Berlin Sans FB Demi\";")
        self.break_btn.setObjectName("break_btn")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.music_bg = QtWidgets.QLabel(self.tab_2)
        self.music_bg.setGeometry(QtCore.QRect(-270, -40, 1051, 581))
        self.music_bg.setText("")
        self.music_bg.setPixmap(QtGui.QPixmap("../Python/BG/maxresdefault2.jpg"))
        self.music_bg.setObjectName("music_bg")
        self.music_btn = QtWidgets.QPushButton(self.tab_2, clicked = lambda: self.play_music_press())
        self.music_btn.setGeometry(QtCore.QRect(530, 90, 191, 61))
        self.music_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(219, 200, 45, 252), stop:1 rgba(209, 255, 137, 252));\n"
"font: 75 14pt \"Berlin Sans FB Demi\";")
        self.music_btn.setObjectName("music_btn")
        self.Random_music_btn = QtWidgets.QPushButton(self.tab_2, clicked = lambda: self.play_random_music())
        self.Random_music_btn.setGeometry(QtCore.QRect(530, 200, 191, 61))
        self.Random_music_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(219, 200, 45, 252), stop:1 rgba(209, 255, 137, 252));\n"
"font: 75 14pt \"Berlin Sans FB Demi\";")
        self.Random_music_btn.setObjectName("Random_music_btn")
        self.Automated_music_btn = QtWidgets.QPushButton(self.tab_2)
        self.Automated_music_btn.setGeometry(QtCore.QRect(530, 300, 191, 61))
        self.Automated_music_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(219, 200, 45, 252), stop:1 rgba(209, 255, 137, 252));\n"
"font: 75 14pt \"Berlin Sans FB Demi\";")
        self.Automated_music_btn.setObjectName("Automated_music_btn")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(520, 20, 211, 21))
        self.label.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 227), stop:0.994737 rgba(0, 0, 0, 252));\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(78, 213, 63, 227), stop:0.994737 rgba(194, 255, 135, 252));")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(500, 40, 241, 20))
        self.label_2.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 227), stop:0.994737 rgba(0, 0, 0, 252));\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(78, 213, 63, 227), stop:0.994737 rgba(194, 255, 135, 252));")
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_2, "")
        Prorest.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Prorest)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 26))
        self.menubar.setObjectName("menubar")
        Prorest.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Prorest)
        self.statusbar.setObjectName("statusbar")
        Prorest.setStatusBar(self.statusbar)

        self.retranslateUi(Prorest)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Prorest)

    def retranslateUi(self, Prorest):
        _translate = QtCore.QCoreApplication.translate
        Prorest.setWindowTitle(_translate("Prorest", "MainWindow"))
        self.break_btn.setToolTip(_translate("Prorest", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Turn on</span></p></body></html>"))
        self.break_btn.setText(_translate("Prorest", "Turn on"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Prorest", "Break reminder"))
        self.music_btn.setToolTip(_translate("Prorest", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Turn on</span></p></body></html>"))
        self.music_btn.setText(_translate("Prorest", "Turn on"))
        self.Random_music_btn.setToolTip(_translate("Prorest", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Turn on</span></p></body></html>"))
        self.Random_music_btn.setText(_translate("Prorest", "Randomize on"))
        self.Automated_music_btn.setToolTip(_translate("Prorest", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Turn on</span></p></body></html>"))
        self.Automated_music_btn.setText(_translate("Prorest", "Set music timer"))
        self.label.setText(_translate("Prorest", "Note! When you turn the music off,"))
        self.label_2.setText(_translate("Prorest", " the current song will need to finish fully."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Prorest", "Relaxing songs"))

    def break_press(self):
        if self.breakChoice == 1:
            self.break_btn.setText("Turn off")
            self.breakChoice = 2
            WorkerThread.running = True
            self.worker = WorkerThread(1)
            self.worker.start()
        else:
            WorkerThread.running = False
            self.break_btn.setText("Turn on")
            self.breakChoice = 1

    def play_music_press(self):
        if self.musicOrder == 1:
            self.music_btn.setText("Turn off")
            self.musicOrder = 2
            WorkerThread.music = True
            self.worker = WorkerThread(2)
            self.worker.start()
        else:
            WorkerThread.music = False
            self.music_btn.setText("Turn on")
            self.musicOrder = 1

    def play_random_music(self):
        if self.musicRandom == 1:
            self.Random_music_btn.setText("Randomize off")
            self.musicRandom = 2
            WorkerThread.randMusic = True
            self.worker = WorkerThread(3)
            self.worker.start()
        else:
            WorkerThread.randMusic = False
            self.Random_music_btn.setText("Randomize on")
            self.musicRandom = 1

class WorkerThread(QThread):
    running = True
    music = True
    randMusic = True

    def __init__(self, workerNum):
        super().__init__()
        self.workerNum = workerNum

    def run(self):
        if self.workerNum == 1:
            while self.running:
                notification.notify(title = "It's time for a small break!",
                                    message = "Why don't you stretch a bit, move your body and rest your eyes :)",
                                    app_name = "Prorest",
                                    app_icon = "Meh.ico",
                                    timeout = 50)
                time.sleep(1800)
        
        elif self.workerNum == 2:
            d = Database()
            songs = d.play_songs_order()
            for song in songs:
                while self.music:
                    video = pafy.new(song)
                    length = video.length
                    best = video.getbestaudio()
                    playurl = best.url
                    instance = vlc.Instance()
                    player = instance.media_player_new()
                    media = instance.media_new(playurl)
                    media.get_mrl()
                    player.set_media(media)
                    player.play()
                    time.sleep(length)
                    player.stop()
                    break

        elif self.workerNum == 3:
            d = Database()
            songs = d.play_songs_order()
            while len(songs) > 0:
                while self.randMusic:
                    randsong = random.randint(0, len(songs)-1)
                    video = pafy.new(songs[randsong])
                    length = video.length
                    best = video.getbestaudio()
                    playurl = best.url
                    instance = vlc.Instance()
                    player = instance.media_player_new()
                    media = instance.media_new(playurl)
                    media.get_mrl()
                    player.set_media(media)
                    player.play()
                    time.sleep(length)
                    player.stop()
                    songs.pop(randsong)
                    break

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Prorest = QtWidgets.QMainWindow()
    ui = Ui_Prorest()
    ui.setupUi(Prorest)
    Prorest.show()
    sys.exit(app.exec_())
