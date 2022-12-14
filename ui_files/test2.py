# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'img_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(884, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.first = QtWidgets.QPushButton(self.centralwidget)
        self.first.setGeometry(QtCore.QRect(0, 380, 91, 41))
        self.first.setObjectName("first")
        self.second = QtWidgets.QPushButton(self.centralwidget)
        self.second.setGeometry(QtCore.QRect(780, 390, 101, 41))
        self.second.setObjectName("second")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(10, 10, 871, 371))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../imgs/cook.png"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 884, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.first.clicked.connect(self.show_first)
        self.second.clicked.connect(self.show_popup)
        # self.second.clicked.connect(self.show_second)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.first.setText(_translate("MainWindow", "1st Picture"))
        self.second.setText(_translate("MainWindow", "2nd Picture"))

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Tutorial on PyQT5")
        msg.setText("This is the main text!")
        # msg.setIcon(QMessageBox.Critical)
        # msg.setIcon(QMessageBox.Warning)
        # msg.setIcon(QMessageBox.Information)
        msg.setIcon(QMessageBox.Question)

        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry|QMessageBox.Ignore)
        msg.setDefaultButton(QMessageBox.Ignore)
        msg.setInformativeText("Information")

        msg.setDetailedText("details")
        msg.buttonClicked.connect(self.popup_button)

        x = msg.exec_()
    
    def popup_button(self, i):
        print(i.text())


        

    def show_first(self):
        self.photo.setPixmap(QtGui.QPixmap("../imgs/cook.png"))

    def show_second(self):
        self.photo.setPixmap(QtGui.QPixmap("../imgs/fish.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
