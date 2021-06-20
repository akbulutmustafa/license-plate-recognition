# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editdia.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(223, 179)
        Dialog.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 130, 181, 32))
        self.buttonBox.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.txtad = QtWidgets.QLineEdit(Dialog)
        self.txtad.setGeometry(QtCore.QRect(60, 30, 113, 20))
        self.txtad.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.txtad.setObjectName("txtad")
        self.txtsoyad = QtWidgets.QLineEdit(Dialog)
        self.txtsoyad.setGeometry(QtCore.QRect(60, 60, 113, 20))
        self.txtsoyad.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.txtsoyad.setObjectName("txtsoyad")
        self.txtplk = QtWidgets.QLineEdit(Dialog)
        self.txtplk.setGeometry(QtCore.QRect(60, 90, 113, 20))
        self.txtplk.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.txtplk.setObjectName("txtplk")
        self.lblad = QtWidgets.QLabel(Dialog)
        self.lblad.setGeometry(QtCore.QRect(10, 30, 47, 13))
        self.lblad.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblad.setObjectName("lblad")
        self.lblsoyad = QtWidgets.QLabel(Dialog)
        self.lblsoyad.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.lblsoyad.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblsoyad.setObjectName("lblsoyad")
        self.lblplk = QtWidgets.QLabel(Dialog)
        self.lblplk.setGeometry(QtCore.QRect(10, 90, 31, 16))
        self.lblplk.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblplk.setObjectName("lblplk")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblad.setText(_translate("Dialog", "Ad"))
        self.lblsoyad.setText(_translate("Dialog", "Soyad"))
        self.lblplk.setText(_translate("Dialog", "Plaka"))

