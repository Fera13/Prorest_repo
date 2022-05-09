# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Prorest10.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from os import sep
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import RunningOp
import time
import schedule
import sys
from Database import *
import random
from datetime import date, timedelta

d = Database()

class Ui_Prorest(QDialog):
    breakChoice = 1
    musicOrder = 1
    musicRandom = 1
    musicTimer = 1
    music_timer_play = 1
    snackChoice = 1
    important_dates = 1
    quote = 1
    
    def setupUi(self, Prorest):
        """The skeleton of the program"""
        Prorest.setObjectName("Prorest")
        Prorest.resize(1075, 826)
        Prorest.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(151, 45, 219, 252), stop:1 rgba(72, 151, 183, 252));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(63, 134, 213, 227), stop:0.994737 rgba(194, 255, 135, 252));")
        self.centralwidget = QtWidgets.QWidget(Prorest)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 1031, 771))
        self.tabWidget.setStyleSheet("font: 75 10pt \"Garamond\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(111, 39, 186, 241), stop:0.994737 rgba(170, 20, 119, 209));\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.break_bg = QtWidgets.QLabel(self.tab)
        self.break_bg.setGeometry(QtCore.QRect(-6, -25, 1031, 771))
        self.break_bg.setText("")
        self.break_bg.setPixmap(QtGui.QPixmap("../Python/BG/ThinkstockPhotos-489763838-e1490767826261.jpg"))
        self.break_bg.setScaledContents(True)
        self.break_bg.setObjectName("break_bg")
        self.break_btn = QtWidgets.QPushButton(self.tab, clicked = lambda: self.break_press())
        self.break_btn.setGeometry(QtCore.QRect(770, 130, 191, 61))
        self.break_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 219, 182, 252), stop:1 rgba(209, 255, 137, 252));\n"
"font: 75 14pt \"Berlin Sans FB Demi\";")
        self.break_btn.setObjectName("break_btn")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.music_bg = QtWidgets.QLabel(self.tab_2)
        self.music_bg.setGeometry(QtCore.QRect(-270, -40, 1301, 781))
        self.music_bg.setText("")
        self.music_bg.setPixmap(QtGui.QPixmap("../Python/BG/maxresdefault2.jpg"))
        self.music_bg.setScaledContents(True)        
        self.music_bg.setObjectName("music_bg")
        self.music_btn = QtWidgets.QPushButton(self.tab_2, clicked = lambda: self.play_music_press())
        self.music_btn.setGeometry(QtCore.QRect(750, 150, 191, 61))
        self.music_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(219, 200, 45, 252), stop:1 rgba(209, 255, 137, 252));\n"
"font: 75 14pt \"Berlin Sans FB Demi\";")
        self.music_btn.setObjectName("music_btn")
        self.Random_music_btn = QtWidgets.QPushButton(self.tab_2, clicked = lambda: self.play_random_music())
        self.Random_music_btn.setGeometry(QtCore.QRect(750, 280, 191, 61))
        self.Random_music_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(219, 200, 45, 252), stop:1 rgba(209, 255, 137, 252));\n"
"font: 75 14pt \"Berlin Sans FB Demi\";")
        self.Random_music_btn.setObjectName("Random_music_btn")
        self.Automated_music_btn = QtWidgets.QPushButton(self.tab_2, clicked = lambda: self.set_music_time_press(self.write_time_bar.text()))
        self.Automated_music_btn.setGeometry(QtCore.QRect(750, 400, 191, 61))
        self.Automated_music_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(219, 200, 45, 252), stop:1 rgba(209, 255, 137, 252));\n"
"font: 75 14pt \"Berlin Sans FB Demi\";")
        self.Automated_music_btn.setObjectName("Automated_music_btn")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(740, 70, 211, 21))
        self.label.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 227), stop:0.994737 rgba(0, 0, 0, 252));\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(78, 213, 63, 227), stop:0.994737 rgba(194, 255, 135, 252));")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(720, 90, 251, 20))
        self.label_2.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 227), stop:0.994737 rgba(0, 0, 0, 252));\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(78, 213, 63, 227), stop:0.994737 rgba(194, 255, 135, 252));")
        self.label_2.setObjectName("label_2")
        self.write_time_bar = QtWidgets.QLineEdit(self.tab_2)
        self.write_time_bar.setGeometry(QtCore.QRect(780, 480, 131, 31))
        self.write_time_bar.setText("")
        self.write_time_bar.setObjectName("write_time_bar")
        self.time_format_label = QtWidgets.QLabel(self.tab_2)
        self.time_format_label.setGeometry(QtCore.QRect(740, 540, 211, 21))
        self.time_format_label.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 227), stop:0.994737 rgba(0, 0, 0, 252));\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(78, 213, 63, 227), stop:0.994737 rgba(194, 255, 135, 252));")
        self.time_format_label.setObjectName("time_format_label")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.snacks_bg = QtWidgets.QLabel(self.tab_3)
        self.snacks_bg.setGeometry(QtCore.QRect(0, 0, 1031, 751))
        self.snacks_bg.setText("")
        self.snacks_bg.setPixmap(QtGui.QPixmap("../Python/BG/bread-toasted_WDGG60RQAJ.jpg"))
        self.snacks_bg.setScaledContents(True)
        self.snacks_bg.setObjectName("snacks_bg")
        self.snacks_btn = QtWidgets.QPushButton(self.tab_3, clicked = lambda: self.snack_press())
        self.snacks_btn.setGeometry(QtCore.QRect(10, 40, 191, 61))
        self.snacks_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 219, 182, 252), stop:1 rgba(209, 255, 137, 252));\n"
"font: 75 14pt \"Berlin Sans FB Demi\";")
        self.snacks_btn.setObjectName("snacks_btn")
        self.snacks_tips = QtWidgets.QLabel(self.tab_3)
        self.snacks_tips.setGeometry(QtCore.QRect(10, 170, 331, 521))
        self.snacks_tips.setStyleSheet("font: 75 12pt \"Berlin Sans FB Demi\";")
        self.snacks_tips.setObjectName("snacks_tips")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.important_bg = QtWidgets.QLabel(self.tab_4)
        self.important_bg.setGeometry(QtCore.QRect(-4, -8, 1031, 751))
        self.important_bg.setText("")
        self.important_bg.setPixmap(QtGui.QPixmap("../Python/BG/woman-writing_FFSUL8TZD3.jpg"))
        self.important_bg.setScaledContents(True)        
        self.important_bg.setObjectName("important_bg")
        self.date_label = QtWidgets.QLabel(self.tab_4)
        self.date_label.setGeometry(QtCore.QRect(100, 70, 211, 21))
        self.date_label.setStyleSheet("font: 75 9pt \"Berlin Sans FB Demi\";")
        self.date_label.setObjectName("date_label")
        self.information_label = QtWidgets.QLabel(self.tab_4)
        self.information_label.setGeometry(QtCore.QRect(30, 10, 371, 21))
        self.information_label.setStyleSheet("font: 75 8pt \"Berlin Sans FB Demi\";")
        self.information_label.setObjectName("information_label")
        self.time_label = QtWidgets.QLabel(self.tab_4)
        self.time_label.setGeometry(QtCore.QRect(100, 150, 211, 21))
        self.time_label.setStyleSheet("font: 75 9pt \"Berlin Sans FB Demi\";")
        self.time_label.setObjectName("time_label")
        self.title_label = QtWidgets.QLabel(self.tab_4)
        self.title_label.setGeometry(QtCore.QRect(100, 230, 211, 21))
        self.title_label.setStyleSheet("font: 75 9pt \"Berlin Sans FB Demi\";")
        self.title_label.setObjectName("title_label")
        self.msg_label = QtWidgets.QLabel(self.tab_4)
        self.msg_label.setGeometry(QtCore.QRect(100, 310, 211, 21))
        self.msg_label.setStyleSheet("font: 75 9pt \"Berlin Sans FB Demi\";")
        self.msg_label.setObjectName("msg_label")
        self.write_date = QtWidgets.QLineEdit(self.tab_4)
        self.write_date.setGeometry(QtCore.QRect(100, 100, 211, 31))
        self.write_date.setText("")
        self.write_date.setObjectName("write_date")
        self.write_time = QtWidgets.QLineEdit(self.tab_4)
        self.write_time.setGeometry(QtCore.QRect(100, 180, 211, 31))
        self.write_time.setText("")
        self.write_time.setObjectName("write_time")
        self.write_title = QtWidgets.QLineEdit(self.tab_4)
        self.write_title.setGeometry(QtCore.QRect(100, 260, 211, 31))
        self.write_title.setText("")
        self.write_title.setObjectName("write_title")
        self.write_message = QtWidgets.QLineEdit(self.tab_4)
        self.write_message.setGeometry(QtCore.QRect(100, 340, 211, 31))
        self.write_message.setText("")
        self.write_message.setObjectName("write_message")
        self.set_date_btn = QtWidgets.QPushButton(self.tab_4, clicked = lambda: self.set_dates_press(self.write_date.text(), self.write_time.text(), self.write_title.text(), self.write_message.text()))
        self.set_date_btn.setGeometry(QtCore.QRect(100, 430, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.set_date_btn.setFont(font)
        self.set_date_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 219, 182, 252), stop:1 rgba(209, 255, 137, 252));\n"
"font: 75 14pt \"Berlin Sans FB Demi\";")
        self.set_date_btn.setObjectName("set_date_btn")
        self.information_label_2 = QtWidgets.QLabel(self.tab_4)
        self.information_label_2.setGeometry(QtCore.QRect(30, 30, 371, 21))
        self.information_label_2.setStyleSheet("font: 75 8pt \"Berlin Sans FB Demi\";")
        self.information_label_2.setObjectName("information_label_2")
        self.time_format_label_2 = QtWidgets.QLabel(self.tab_4)
        self.time_format_label_2.setGeometry(QtCore.QRect(100, 390, 211, 21))
        self.time_format_label_2.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 227), stop:0.994737 rgba(0, 0, 0, 252));\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(78, 213, 63, 227), stop:0.994737 rgba(194, 255, 135, 252));")
        self.time_format_label_2.setObjectName("time_format_label_2")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.quote_label = QtWidgets.QLabel(self.tab_6)
        self.quote_label.setGeometry(QtCore.QRect(0, 0, 1031, 751))
        self.quote_label.setText("")
        self.quote_label.setPixmap(QtGui.QPixmap("../Python/BG/funny.jpg"))
        self.quote_label.setScaledContents(True)
        self.quote_label.setObjectName("quote_label")
        self.quote_label_1 = QtWidgets.QLabel(self.tab_6)
        self.quote_label_1.setGeometry(QtCore.QRect(690, 490, 251, 41))
        self.quote_label_1.setObjectName("quote_label_1")
        self.set_quote_btn = QtWidgets.QPushButton(self.tab_6, clicked = lambda: self.set_quotes_press(self.write_quote.text()))
        self.set_quote_btn.setGeometry(QtCore.QRect(640, 650, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.set_quote_btn.setFont(font)
        self.set_quote_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 219, 182, 252), stop:1 rgba(209, 255, 137, 252));\n"
"font: 75 14pt \"Berlin Sans FB Demi\";")
        self.set_quote_btn.setObjectName("set_quote_btn")
        self.quote_btn = QtWidgets.QPushButton(self.tab_6, clicked = lambda: self.quote_press())
        self.quote_btn.setGeometry(QtCore.QRect(60, 590, 191, 61))
        self.quote_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 219, 182, 252), stop:1 rgba(209, 255, 137, 252));\n"
"font: 75 14pt \"Berlin Sans FB Demi\";")
        self.quote_btn.setObjectName("quote_btn")
        self.write_quote = QtWidgets.QLineEdit(self.tab_6)
        self.write_quote.setGeometry(QtCore.QRect(640, 560, 351, 51))
        self.write_quote.setText("")
        self.write_quote.setObjectName("write_quote")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_3 = QtWidgets.QLabel(self.tab_5)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1031, 751))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../Python/BG/books-library_6XANS2384I.jpg"))
        self.label_3.setScaledContents(True)        
        self.label_3.setObjectName("label_3")
        self.resourse_label = QtWidgets.QLabel(self.tab_5)
        self.resourse_label.setGeometry(QtCore.QRect(189, 490, 821, 240))
        self.resourse_label.setStyleSheet("font: 75 10pt \"Berlin Sans FB Demi\";")
        self.resourse_label.setObjectName("resourse_label")
        self.tabWidget.addTab(self.tab_5, "")
        Prorest.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Prorest)
        self.statusbar.setObjectName("statusbar")
        Prorest.setStatusBar(self.statusbar)
        
        self.retranslateUi(Prorest)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Prorest)
        self.notify_important_dates()

    def retranslateUi(self, Prorest):
        """Texts on the buttons and labels"""
        _translate = QtCore.QCoreApplication.translate
        Prorest.setWindowTitle(_translate("Prorest", "Prorest"))
        self.break_btn.setToolTip(_translate("Prorest", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Turn on</span></p></body></html>"))
        self.break_btn.setText(_translate("Prorest", "Turn on"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Prorest", "Break reminder"))
        self.music_btn.setToolTip(_translate("Prorest", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Turn on</span></p></body></html>"))
        self.music_btn.setText(_translate("Prorest", "Turn on"))
        self.Random_music_btn.setToolTip(_translate("Prorest", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Turn on</span></p></body></html>"))
        self.Random_music_btn.setText(_translate("Prorest", "Randomize on"))
        self.Automated_music_btn.setToolTip(_translate("Prorest", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Turn on</span></p></body></html>"))
        self.Automated_music_btn.setText(_translate("Prorest", "Set music timer"))
        self.label.setText(_translate("Prorest", " Note! When you turn the music off,"))
        self.label_2.setText(_translate("Prorest", "  the current song will need to finish fully."))
        self.time_format_label.setText(_translate("Prorest", "              Format (HH:MM)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Prorest", "Relaxing songs"))
        self.snacks_btn.setToolTip(_translate("Prorest", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Turn on</span></p></body></html>"))
        self.snacks_btn.setText(_translate("Prorest", "Turn on"))
        self.snacks_tips.setText(_translate("Prorest", d.snack_recommendations()))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Prorest", "Snacks and Drink reminder"))
        self.date_label.setText(_translate("Prorest", " Date (Format: YYYY-MM-DD)"))
        self.information_label.setText(_translate("Prorest", "  Add the information with the correct format in the boxes below"))
        self.time_label.setText(_translate("Prorest", "      Time (Format: HH:MM)"))
        self.title_label.setText(_translate("Prorest", "                      Title"))
        self.msg_label.setText(_translate("Prorest", "                   Message"))
        self.set_date_btn.setToolTip(_translate("Prorest", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">Turn on</span></p></body></html>"))
        self.set_date_btn.setText(_translate("Prorest", "Set Date Reminder"))
        self.information_label_2.setText(_translate("Prorest", "         When you are done, click on the button in the bottom."))
        self.time_format_label_2.setText(_translate("Prorest", "           Is it in a right Format ?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Prorest", "Important Dates"))
        self.resourse_label.setText(_translate("Prorest", d.read_references()))
        self.quote_label_1.setText(_translate("Prorest", "    You can enter your funny quotes"))
        self.set_quote_btn.setToolTip(_translate("Prorest", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">Turn on</span></p></body></html>"))
        self.set_quote_btn.setText(_translate("Prorest", "Set a Quote"))
        self.quote_btn.setToolTip(_translate("Prorest", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Turn on</span></p></body></html>"))
        self.quote_btn.setText(_translate("Prorest", "Turn on"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Prorest", "Funny Messages"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Prorest", "Resources"))

    def break_press(self):
        """Check if the requirments are met and start or stop the break notifications"""
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
        """Check if the requirments are met and start or stop playing music in order"""
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
        """Check if the requirments are met and start or stop playing music in a random order"""
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
            
    def set_music_time_press(self, timeSelected):
        """Take the time selected. Check if the requirments are met and start or stop checking current time to play music automatically"""
        timeCheck = RunningOp.checkTimeFormat(timeSelected)
        if timeCheck:
            if self.musicTimer == 1:
                self.Automated_music_btn.setText("Stop timer/ music")
                self.time_format_label.setText("           Time has been set")
                self.musicTimer = 2
                WorkerThread.sTimer = True
                WorkerThread.keepGoing = True
                WorkerThread.timeChosen = timeSelected
                self.worker = WorkerThread(4)
                self.worker.start()
            else:
                self.Automated_music_btn.setText("Set music timer")
                self.time_format_label.setText("              Format (HH:MM)")
                self.write_time_bar.setText("")
                self.musicTimer = 1
                WorkerThread.sTimer = False
                WorkerThread.keepGoing = False
                WorkerThread.songTimer = False
        else:
            self.time_format_label.setText("Please use the right format (HH:MM)")
            self.write_time_bar.setText("")
            
    def timer_song_play(self):
        """Start the music automatically when the time selected matches the current time"""
        WorkerThread.songTimer = True
        self.music_timer_play = 2
        self.worker = WorkerThread(5)
        self.worker.start()
    
    def snack_recommend(self, text):
        """Applies the text to the label"""
        self.snacks_tips.setText(text)
        
    def snack_press(self):
        """Check if the requirments are met and start or stop the snack notifications"""
        if self.snackChoice == 1:
            self.snacks_btn.setText("Turn off")
            self.snackChoice = 2
            WorkerThread.snack = True
            self.worker = WorkerThread(6)
            self.worker.start()
        else:
            WorkerThread.snack = False
            self.snacks_btn.setText("Turn on")
            self.snackChoice = 1
            
    def set_dates_press(self, date, time, title, msg):
        """Set an important date """
        d = Database()
        dateCheck = RunningOp.check_date_format(date)
        timeCheck = RunningOp.checkTimeFormat(time)
        if dateCheck & timeCheck:
                d.write_important(date, time, title, msg)
                self.time_format_label_2.setText("           Is it in a right Format ?")
        else: 
            self.time_format_label_2.setText("      Check date and time format !")
    
    def notify_important_dates(self):
        tomorrow_dates = d.check_important_dates()
        if tomorrow_dates == []:
            WorkerThread.date = False
        else:
            WorkerThread.date = True
            self.worker = WorkerThread(7)
            self.worker.start()
            
    def set_quotes_press(self, quote):
        """Set a quote in database"""
        d = Database()
        if self.quote == 1:
            d.write_quote(quote)
        
    def quote_press(self):
        """Start or stop the quote notifications"""
        if self.quote == 1:
            self.quote_btn.setText("Turn off")
            self.quote = 2
            WorkerThread.quote = True
            self.worker = WorkerThread(8)
            self.worker.start()
        else:
            WorkerThread.quote = False
            self.quote_btn.setText("Turn on")
            self.quote = 1

class WorkerThread(QThread):
    running = True
    music = True
    randMusic = True
    songTimer = True
    keepGoing = True
    sTimer = True
    timeChosen = ""
    snack = True
    date = True
    quote = True

    def __init__(self, workerNum):
        super().__init__()
        self.workerNum = workerNum

    def run(self):
        """Starts running different workers depending on the conditions and can be activated together or separatly"""
        if self.workerNum == 1:
            while self.running:
                RunningOp.viewNotification("It's time for a small break!", "Why don't you stretch a bit, move your body and rest your eyes :)", "Icons/Meh.ico", 50, 1800)
        
        elif self.workerNum == 2:
            d = Database()
            songs = d.play_songs_order()
            for song in songs:
                while self.music:
                    RunningOp.play_music(song)
                    break

        elif self.workerNum == 3:
            d = Database()
            songs = d.play_songs_order()
            while len(songs) > 0:
                while self.randMusic:
                    randsong = random.randint(0, len(songs)-1)
                    RunningOp.play_music(songs[randsong])
                    songs.pop(randsong)
    
        elif self.workerNum == 4:
            while self.sTimer:
                u = Ui_Prorest()
                schedule.every().day.at(self.timeChosen).do(u.timer_song_play)
                while self.keepGoing:
                    schedule.run_pending()
                    time.sleep(1)

        elif self.workerNum == 5:
            d = Database()
            songs = d.play_songs_order()
            while len(songs) > 0:
                while self.songTimer:
                    randsong = random.randint(0, len(songs)-1)
                    RunningOp.play_music(songs[randsong])
                    songs.pop(randsong)
        
        elif self.workerNum == 6:
            while self.snack:
                RunningOp.viewNotification("It's time for some snacks and refreshments!", "Why don't you grab yourself a snack and some water? Give yourself some much needed energy :)", "Icons/1.ico", 60, 7200)

        elif self.workerNum == 7:
            d = Database()
            RunningOp.viewDateNotification(d.read_important(date.today() + timedelta(days = 1)), "Icons/2.ico", 60)
        
        elif self.workerNum == 8:
            d = Database()
            while self.quote:
                RunningOp.viewQuoteNotification(d.read_quotes(), "Icons/3.ico", 30, 5400)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Prorest = QtWidgets.QMainWindow()
    ui = Ui_Prorest()
    ui.setupUi(Prorest)
    Prorest.show()
    sys.exit(app.exec_())
