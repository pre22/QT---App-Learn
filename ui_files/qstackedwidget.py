# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qstackediwdget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 605)
        MainWindow.setStyleSheet("background-color: rgb(233, 226, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 50, 821, 431))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Home.setObjectName("Home")
        self.label = QtWidgets.QLabel(self.Home)
        self.label.setGeometry(QtCore.QRect(140, 230, 511, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.Home)
        self.Blue = QtWidgets.QWidget()
        self.Blue.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.Blue.setObjectName("Blue")
        self.stackedWidget.addWidget(self.Blue)
        self.Red = QtWidgets.QWidget()
        self.Red.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Red.setObjectName("Red")
        self.stackedWidget.addWidget(self.Red)
        self.Yellow = QtWidgets.QWidget()
        self.Yellow.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.Yellow.setObjectName("Yellow")
        self.stackedWidget.addWidget(self.Yellow)
        self.BlueButton = QtWidgets.QPushButton(self.centralwidget)
        self.BlueButton.setGeometry(QtCore.QRect(140, 510, 91, 31))
        self.BlueButton.setObjectName("BlueButton")
        self.RedButton = QtWidgets.QPushButton(self.centralwidget)
        self.RedButton.setGeometry(QtCore.QRect(410, 510, 91, 31))
        self.RedButton.setObjectName("RedButton")
        self.YellowBUtton = QtWidgets.QPushButton(self.centralwidget)
        self.YellowBUtton.setGeometry(QtCore.QRect(680, 510, 91, 31))
        self.YellowBUtton.setObjectName("YellowBUtton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 864, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Please click the buttons below to swtich betweering windows"))
        self.BlueButton.setText(_translate("MainWindow", "Blue"))
        self.RedButton.setText(_translate("MainWindow", "Red"))
        self.YellowBUtton.setText(_translate("MainWindow", "Yellow"))
