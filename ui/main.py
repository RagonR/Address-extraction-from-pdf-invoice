# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Sat Oct 20 10:16:24 2018
#      by: pyside2-uic  running on PySide2 5.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, FileBrowser):
        FileBrowser.setObjectName("File browser")
        FileBrowser.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(FileBrowser)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.treeView = QtWidgets.QTreeView(self.frame)
        self.treeView.setObjectName("treeView")
        self.gridLayout_2.addWidget(self.treeView, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        FileBrowser.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FileBrowser)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        FileBrowser.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FileBrowser)
        self.statusbar.setObjectName("statusbar")
        FileBrowser.setStatusBar(self.statusbar)

        self.retranslateUi(FileBrowser)
        QtCore.QMetaObject.connectSlotsByName(FileBrowser)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "File browser", None, -1))
