# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoRadioButton1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 60, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelFare = QtWidgets.QLabel(Dialog)
        self.labelFare.setGeometry(QtCore.QRect(160, 360, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelFare.setFont(font)
        self.labelFare.setText("")
        self.labelFare.setObjectName("labelFare")
        self.radioButtonFirstClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonFirstClass.setGeometry(QtCore.QRect(70, 180, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButtonFirstClass.setFont(font)
        self.radioButtonFirstClass.setObjectName("radioButtonFirstClass")
        self.radioButtonSecondClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonSecondClass.setGeometry(QtCore.QRect(70, 220, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButtonSecondClass.setFont(font)
        self.radioButtonSecondClass.setObjectName("radioButtonSecondClass")
        self.radioButtonEconomyClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonEconomyClass.setGeometry(QtCore.QRect(70, 260, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButtonEconomyClass.setFont(font)
        self.radioButtonEconomyClass.setObjectName("radioButtonEconomyClass")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose the Flight Type"))
        self.radioButtonFirstClass.setText(_translate("Dialog", "First Class $150"))
        self.radioButtonSecondClass.setText(_translate("Dialog", "Business Class $150"))
        self.radioButtonEconomyClass.setText(_translate("Dialog", "Economy Class $100"))
