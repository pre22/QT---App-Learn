# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCheckBox2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(780, 719)
        font = QtGui.QFont()
        font.setPointSize(14)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(370, 10, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.labelAmount = QtWidgets.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(30, 580, 651, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAmount.setFont(font)
        self.labelAmount.setText("")
        self.labelAmount.setObjectName("labelAmount")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 360, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.groupBoxDrinks = QtWidgets.QGroupBox(Dialog)
        self.groupBoxDrinks.setGeometry(QtCore.QRect(260, 340, 161, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBoxDrinks.setFont(font)
        self.groupBoxDrinks.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBoxDrinks.setCheckable(True)
        self.groupBoxDrinks.setObjectName("groupBoxDrinks")
        self.widget = QtWidgets.QWidget(self.groupBoxDrinks)
        self.widget.setGeometry(QtCore.QRect(30, 50, 94, 95))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxCoffee = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBoxCoffee.setFont(font)
        self.checkBoxCoffee.setObjectName("checkBoxCoffee")
        self.verticalLayout.addWidget(self.checkBoxCoffee)
        self.checkBoxTea = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBoxTea.setFont(font)
        self.checkBoxTea.setObjectName("checkBoxTea")
        self.verticalLayout.addWidget(self.checkBoxTea)
        self.checkBoxSoda = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBoxSoda.setFont(font)
        self.checkBoxSoda.setObjectName("checkBoxSoda")
        self.verticalLayout.addWidget(self.checkBoxSoda)
        self.groupBoxIceCreams = QtWidgets.QGroupBox(Dialog)
        self.groupBoxIceCreams.setGeometry(QtCore.QRect(260, 80, 271, 211))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBoxIceCreams.setFont(font)
        self.groupBoxIceCreams.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBoxIceCreams.setCheckable(True)
        self.groupBoxIceCreams.setObjectName("groupBoxIceCreams")
        self.widget1 = QtWidgets.QWidget(self.groupBoxIceCreams)
        self.widget1.setGeometry(QtCore.QRect(40, 140, 201, 62))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.widget1.setFont(font)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBoxRockyRoad = QtWidgets.QCheckBox(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBoxRockyRoad.setFont(font)
        self.checkBoxRockyRoad.setObjectName("checkBoxRockyRoad")
        self.verticalLayout_3.addWidget(self.checkBoxRockyRoad)
        self.checkBoxChocolateAlmond = QtWidgets.QCheckBox(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBoxChocolateAlmond.setFont(font)
        self.checkBoxChocolateAlmond.setObjectName("checkBoxChocolateAlmond")
        self.verticalLayout_3.addWidget(self.checkBoxChocolateAlmond)
        self.widget2 = QtWidgets.QWidget(self.groupBoxIceCreams)
        self.widget2.setGeometry(QtCore.QRect(40, 60, 225, 62))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.widget2.setFont(font)
        self.widget2.setObjectName("widget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBoxChocolateChips = QtWidgets.QCheckBox(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBoxChocolateChips.setFont(font)
        self.checkBoxChocolateChips.setObjectName("checkBoxChocolateChips")
        self.verticalLayout_2.addWidget(self.checkBoxChocolateChips)
        self.checkBoxCookieDough = QtWidgets.QCheckBox(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBoxCookieDough.setFont(font)
        self.checkBoxCookieDough.setObjectName("checkBoxCookieDough")
        self.verticalLayout_2.addWidget(self.checkBoxCookieDough)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Menu"))
        self.label_2.setText(_translate("Dialog", "Select Your IceCream"))
        self.label_4.setText(_translate("Dialog", "Select your drink"))
        self.groupBoxDrinks.setTitle(_translate("Dialog", "drinks"))
        self.checkBoxCoffee.setText(_translate("Dialog", "Coffe $2"))
        self.checkBoxTea.setText(_translate("Dialog", "Tea $1"))
        self.checkBoxSoda.setText(_translate("Dialog", "Soda $3"))
        self.groupBoxIceCreams.setTitle(_translate("Dialog", "Ice Cream"))
        self.checkBoxRockyRoad.setText(_translate("Dialog", "Rocky Road $5"))
        self.checkBoxChocolateAlmond.setText(_translate("Dialog", "Chocolate Almond $3"))
        self.checkBoxChocolateChips.setText(_translate("Dialog", "Mint Chocolate Chips $4"))
        self.checkBoxCookieDough.setText(_translate("Dialog", "Cookie Dough $2"))
