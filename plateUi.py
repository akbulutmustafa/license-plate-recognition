# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plateUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(785, 465)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(10, 10, 611, 401))
        self.img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img.setText("")
        self.img.setScaledContents(True)
        self.img.setObjectName("img")
        self.plateFind = QtWidgets.QPushButton(self.centralwidget)
        self.plateFind.setGeometry(QtCore.QRect(640, 60, 131, 31))
        self.plateFind.setObjectName("plateFind")
        self.imchoose = QtWidgets.QPushButton(self.centralwidget)
        self.imchoose.setGeometry(QtCore.QRect(640, 10, 131, 31))
        self.imchoose.setObjectName("imchoose")
        self.readPlate = QtWidgets.QPushButton(self.centralwidget)
        self.readPlate.setGeometry(QtCore.QRect(640, 110, 131, 31))
        self.readPlate.setObjectName("readPlate")
        self.platetxt = QtWidgets.QLabel(self.centralwidget)
        self.platetxt.setGeometry(QtCore.QRect(640, 160, 131, 41))
        self.platetxt.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.platetxt.setFrameShadow(QtWidgets.QFrame.Raised)
        self.platetxt.setText("")
        self.platetxt.setObjectName("platetxt")
        self.gray = QtWidgets.QPushButton(self.centralwidget)
        self.gray.setGeometry(QtCore.QRect(710, 290, 61, 23))
        self.gray.setObjectName("gray")
        self.thresh = QtWidgets.QPushButton(self.centralwidget)
        self.thresh.setGeometry(QtCore.QRect(640, 320, 61, 23))
        self.thresh.setObjectName("thresh")
        self.blur = QtWidgets.QPushButton(self.centralwidget)
        self.blur.setGeometry(QtCore.QRect(710, 320, 61, 23))
        self.blur.setObjectName("blur")
        self.rgb = QtWidgets.QPushButton(self.centralwidget)
        self.rgb.setGeometry(QtCore.QRect(640, 290, 61, 21))
        self.rgb.setObjectName("rgb")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(636, 352, 141, 51))
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.opencam = QtWidgets.QPushButton(self.centralwidget)
        self.opencam.setGeometry(QtCore.QRect(640, 220, 131, 31))
        self.opencam.setObjectName("opencam")
        self.savecam = QtWidgets.QPushButton(self.centralwidget)
        self.savecam.setGeometry(QtCore.QRect(660, 250, 91, 23))
        self.savecam.setObjectName("savecam")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 785, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plaka Tanıma Sistemi"))
        self.plateFind.setText(_translate("MainWindow", "Plakayı Bul"))
        self.imchoose.setText(_translate("MainWindow", "Resim Seç"))
        self.readPlate.setText(_translate("MainWindow", "Plakayı Oku"))
        self.gray.setText(_translate("MainWindow", "Gray"))
        self.thresh.setText(_translate("MainWindow", "Thresh"))
        self.blur.setText(_translate("MainWindow", "BTW Not"))
        self.rgb.setText(_translate("MainWindow", "Original"))
        self.opencam.setText(_translate("MainWindow", "Kamerayı Aç"))
        self.savecam.setText(_translate("MainWindow", "Kareyi Seç"))