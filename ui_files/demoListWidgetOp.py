# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoListWidgetOp.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(887, 391)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 70, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 70, 241, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButtonAdd = QtWidgets.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(260, 140, 75, 31))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(490, 50, 371, 241))
        self.listWidget.setObjectName("listWidget")
        self.pushButtonEdit = QtWidgets.QPushButton(Dialog)
        self.pushButtonEdit.setGeometry(QtCore.QRect(484, 330, 81, 31))
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.pushButtonDeleteAll = QtWidgets.QPushButton(Dialog)
        self.pushButtonDeleteAll.setGeometry(QtCore.QRect(784, 330, 81, 31))
        self.pushButtonDeleteAll.setObjectName("pushButtonDeleteAll")
        self.pushButtonDelete = QtWidgets.QPushButton(Dialog)
        self.pushButtonDelete.setGeometry(QtCore.QRect(634, 330, 81, 31))
        self.pushButtonDelete.setObjectName("pushButtonDelete")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter an item"))
        self.pushButtonAdd.setText(_translate("Dialog", "Add"))
        self.pushButtonEdit.setText(_translate("Dialog", "Edit"))
        self.pushButtonDeleteAll.setText(_translate("Dialog", "Delete All"))
        self.pushButtonDelete.setText(_translate("Dialog", "Delete"))
