# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'todolist.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))
        MainWindow.setStyleSheet("")
        self.AddButton = QtWidgets.QPushButton(MainWindow)
        self.AddButton.setGeometry(QtCore.QRect(750, 80, 41, 41))
        self.AddButton.setObjectName("AddButton")
        self.RemoveButton = QtWidgets.QPushButton(MainWindow)
        self.RemoveButton.setGeometry(QtCore.QRect(750, 180, 41, 41))
        self.RemoveButton.setObjectName("RemoveButton")
        self.AddSubButton = QtWidgets.QPushButton(MainWindow)
        self.AddSubButton.setGeometry(QtCore.QRect(750, 130, 41, 41))
        self.AddSubButton.setObjectName("AddSubButton")
        self.treeView = QtWidgets.QTreeView(MainWindow)
        self.treeView.setGeometry(QtCore.QRect(9, 82, 731, 401))
        self.treeView.setMinimumSize(QtCore.QSize(500, 400))
        self.treeView.setStyleSheet("QTreeView::item {\n"
"    height: 30;\n"
"    width: 20;\n"
"    font: 87 14pt \"Arial\";\n"
"}\n"
"")
        self.treeView.setObjectName("treeView")
        self.MoveUpButton = QtWidgets.QPushButton(MainWindow)
        self.MoveUpButton.setGeometry(QtCore.QRect(750, 260, 41, 41))
        self.MoveUpButton.setObjectName("MoveUpButton")
        self.MoveDownButton = QtWidgets.QPushButton(MainWindow)
        self.MoveDownButton.setGeometry(QtCore.QRect(750, 310, 41, 41))
        self.MoveDownButton.setObjectName("MoveDownButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TodoList"))
        self.AddButton.setText(_translate("MainWindow", "+"))
        self.RemoveButton.setText(_translate("MainWindow", "✕"))
        self.AddSubButton.setText(_translate("MainWindow", "↳"))
        self.MoveUpButton.setText(_translate("MainWindow", "↑"))
        self.MoveDownButton.setText(_translate("MainWindow", "↓"))

