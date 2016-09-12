# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogswv.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 450)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setGeometry(QtCore.QRect(30, 340, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 67, 17))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 113, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.graphicsView = PlotWidget(self.widget)
        self.graphicsView.setMaximumSize(QtCore.QSize(640, 16777215))
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_2.addWidget(self.graphicsView)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(100, 0, 100, 0)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.pushButton_3.setText(_translate("Dialog", "PushButton"))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))

from pyqtgraph import PlotWidget
