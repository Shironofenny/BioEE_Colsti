# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Title = QtWidgets.QWidget(self.centralwidget)
        self.Title.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Title.setObjectName("Title")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Title)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.Title)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.Title)
        self.Content = QtWidgets.QWidget(self.centralwidget)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Electrode = QtWidgets.QWidget(self.Content)
        self.Electrode.setMaximumSize(QtCore.QSize(200, 800))
        self.Electrode.setObjectName("Electrode")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Electrode)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.Electrode)
        self.widget.setMinimumSize(QtCore.QSize(0, 200))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 700))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setObjectName("tabWidget")
        self.read = QtWidgets.QWidget()
        self.read.setObjectName("read")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.read)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Status = QtWidgets.QWidget(self.read)
        self.Status.setObjectName("Status")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Status)
        self.horizontalLayout_5.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.Status)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.leStatus = QtWidgets.QLineEdit(self.Status)
        self.leStatus.setReadOnly(True)
        self.leStatus.setObjectName("leStatus")
        self.horizontalLayout_5.addWidget(self.leStatus)
        self.verticalLayout_6.addWidget(self.Status)
        self.Refrence = QtWidgets.QWidget(self.read)
        self.Refrence.setObjectName("Refrence")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Refrence)
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.Refrence)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.leRE = QtWidgets.QLineEdit(self.Refrence)
        self.leRE.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leRE.setReadOnly(True)
        self.leRE.setObjectName("leRE")
        self.horizontalLayout_6.addWidget(self.leRE)
        self.verticalLayout_6.addWidget(self.Refrence)
        self.Counter = QtWidgets.QWidget(self.read)
        self.Counter.setObjectName("Counter")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Counter)
        self.horizontalLayout_7.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.Counter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.leCE = QtWidgets.QLineEdit(self.Counter)
        self.leCE.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leCE.setReadOnly(True)
        self.leCE.setObjectName("leCE")
        self.horizontalLayout_7.addWidget(self.leCE)
        self.verticalLayout_6.addWidget(self.Counter)
        self.Working1 = QtWidgets.QWidget(self.read)
        self.Working1.setObjectName("Working1")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.Working1)
        self.horizontalLayout_9.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.Working1)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.leWE1 = QtWidgets.QLineEdit(self.Working1)
        self.leWE1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leWE1.setReadOnly(True)
        self.leWE1.setObjectName("leWE1")
        self.horizontalLayout_9.addWidget(self.leWE1)
        self.verticalLayout_6.addWidget(self.Working1)
        self.Working2 = QtWidgets.QWidget(self.read)
        self.Working2.setObjectName("Working2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.Working2)
        self.horizontalLayout_8.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.Working2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.leWE2 = QtWidgets.QLineEdit(self.Working2)
        self.leWE2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leWE2.setReadOnly(True)
        self.leWE2.setObjectName("leWE2")
        self.horizontalLayout_8.addWidget(self.leWE2)
        self.verticalLayout_6.addWidget(self.Working2)
        self.Extra1 = QtWidgets.QWidget(self.read)
        self.Extra1.setObjectName("Extra1")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.Extra1)
        self.horizontalLayout_10.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.Extra1)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.leEx1 = QtWidgets.QLineEdit(self.Extra1)
        self.leEx1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leEx1.setReadOnly(True)
        self.leEx1.setObjectName("leEx1")
        self.horizontalLayout_10.addWidget(self.leEx1)
        self.verticalLayout_6.addWidget(self.Extra1)
        self.Extra2 = QtWidgets.QWidget(self.read)
        self.Extra2.setObjectName("Extra2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.Extra2)
        self.horizontalLayout_11.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.Extra2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        self.leEx2 = QtWidgets.QLineEdit(self.Extra2)
        self.leEx2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leEx2.setReadOnly(True)
        self.leEx2.setObjectName("leEx2")
        self.horizontalLayout_11.addWidget(self.leEx2)
        self.verticalLayout_6.addWidget(self.Extra2)
        self.Extra3 = QtWidgets.QWidget(self.read)
        self.Extra3.setObjectName("Extra3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.Extra3)
        self.horizontalLayout_12.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_9 = QtWidgets.QLabel(self.Extra3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_12.addWidget(self.label_9)
        self.leEx3 = QtWidgets.QLineEdit(self.Extra3)
        self.leEx3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leEx3.setReadOnly(True)
        self.leEx3.setObjectName("leEx3")
        self.horizontalLayout_12.addWidget(self.leEx3)
        self.verticalLayout_6.addWidget(self.Extra3)
        self.Extra4 = QtWidgets.QWidget(self.read)
        self.Extra4.setObjectName("Extra4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.Extra4)
        self.horizontalLayout_13.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_10 = QtWidgets.QLabel(self.Extra4)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_13.addWidget(self.label_10)
        self.leEx4 = QtWidgets.QLineEdit(self.Extra4)
        self.leEx4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leEx4.setReadOnly(True)
        self.leEx4.setObjectName("leEx4")
        self.horizontalLayout_13.addWidget(self.leEx4)
        self.verticalLayout_6.addWidget(self.Extra4)
        self.tabWidget.addTab(self.read, "")
        self.set = QtWidgets.QWidget()
        self.set.setObjectName("set")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.set)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.setRE = QtWidgets.QWidget(self.set)
        self.setRE.setObjectName("setRE")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.setRE)
        self.horizontalLayout_14.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pbSetRE = QtWidgets.QPushButton(self.setRE)
        self.pbSetRE.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pbSetRE.setObjectName("pbSetRE")
        self.horizontalLayout_14.addWidget(self.pbSetRE)
        self.leSetRE = QtWidgets.QLineEdit(self.setRE)
        self.leSetRE.setMaximumSize(QtCore.QSize(90, 16777215))
        self.leSetRE.setObjectName("leSetRE")
        self.horizontalLayout_14.addWidget(self.leSetRE)
        self.verticalLayout_7.addWidget(self.setRE)
        self.setWE1 = QtWidgets.QWidget(self.set)
        self.setWE1.setObjectName("setWE1")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.setWE1)
        self.horizontalLayout_15.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pbSetWE1 = QtWidgets.QPushButton(self.setWE1)
        self.pbSetWE1.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pbSetWE1.setObjectName("pbSetWE1")
        self.horizontalLayout_15.addWidget(self.pbSetWE1)
        self.leSetWE1 = QtWidgets.QLineEdit(self.setWE1)
        self.leSetWE1.setMaximumSize(QtCore.QSize(90, 16777215))
        self.leSetWE1.setObjectName("leSetWE1")
        self.horizontalLayout_15.addWidget(self.leSetWE1)
        self.verticalLayout_7.addWidget(self.setWE1)
        self.setWe2 = QtWidgets.QWidget(self.set)
        self.setWe2.setObjectName("setWe2")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.setWe2)
        self.horizontalLayout_16.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pbSetWE2 = QtWidgets.QPushButton(self.setWe2)
        self.pbSetWE2.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pbSetWE2.setObjectName("pbSetWE2")
        self.horizontalLayout_16.addWidget(self.pbSetWE2)
        self.leSetWE2 = QtWidgets.QLineEdit(self.setWe2)
        self.leSetWE2.setMaximumSize(QtCore.QSize(90, 16777215))
        self.leSetWE2.setObjectName("leSetWE2")
        self.horizontalLayout_16.addWidget(self.leSetWE2)
        self.verticalLayout_7.addWidget(self.setWe2)
        self.switchWE = QtWidgets.QWidget(self.set)
        self.switchWE.setObjectName("switchWE")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.switchWE)
        self.horizontalLayout_17.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.pbSwWe1 = QtWidgets.QPushButton(self.switchWE)
        self.pbSwWe1.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pbSwWe1.setCheckable(True)
        self.pbSwWe1.setChecked(False)
        self.pbSwWe1.setObjectName("pbSwWe1")
        self.horizontalLayout_17.addWidget(self.pbSwWe1)
        self.pbSwWe2 = QtWidgets.QPushButton(self.switchWE)
        self.pbSwWe2.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pbSwWe2.setCheckable(True)
        self.pbSwWe2.setObjectName("pbSwWe2")
        self.horizontalLayout_17.addWidget(self.pbSwWe2)
        self.verticalLayout_7.addWidget(self.switchWE)
        self.switchEx = QtWidgets.QWidget(self.set)
        self.switchEx.setObjectName("switchEx")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.switchEx)
        self.horizontalLayout_18.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.pbSwEx1 = QtWidgets.QPushButton(self.switchEx)
        self.pbSwEx1.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pbSwEx1.setCheckable(True)
        self.pbSwEx1.setObjectName("pbSwEx1")
        self.horizontalLayout_18.addWidget(self.pbSwEx1)
        self.pbSwEx2 = QtWidgets.QPushButton(self.switchEx)
        self.pbSwEx2.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pbSwEx2.setCheckable(True)
        self.pbSwEx2.setObjectName("pbSwEx2")
        self.horizontalLayout_18.addWidget(self.pbSwEx2)
        self.verticalLayout_7.addWidget(self.switchEx)
        self.enableADC1 = QtWidgets.QWidget(self.set)
        self.enableADC1.setObjectName("enableADC1")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.enableADC1)
        self.horizontalLayout_19.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.pbEnADC5 = QtWidgets.QPushButton(self.enableADC1)
        self.pbEnADC5.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pbEnADC5.setCheckable(True)
        self.pbEnADC5.setObjectName("pbEnADC5")
        self.horizontalLayout_19.addWidget(self.pbEnADC5)
        self.pbEnADC6 = QtWidgets.QPushButton(self.enableADC1)
        self.pbEnADC6.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pbEnADC6.setCheckable(True)
        self.pbEnADC6.setObjectName("pbEnADC6")
        self.horizontalLayout_19.addWidget(self.pbEnADC6)
        self.verticalLayout_7.addWidget(self.enableADC1)
        self.enableADC2 = QtWidgets.QWidget(self.set)
        self.enableADC2.setObjectName("enableADC2")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.enableADC2)
        self.horizontalLayout_20.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.pbEnADC7 = QtWidgets.QPushButton(self.enableADC2)
        self.pbEnADC7.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pbEnADC7.setCheckable(True)
        self.pbEnADC7.setObjectName("pbEnADC7")
        self.horizontalLayout_20.addWidget(self.pbEnADC7)
        self.pbEnADC8 = QtWidgets.QPushButton(self.enableADC2)
        self.pbEnADC8.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pbEnADC8.setCheckable(True)
        self.pbEnADC8.setObjectName("pbEnADC8")
        self.horizontalLayout_20.addWidget(self.pbEnADC8)
        self.verticalLayout_7.addWidget(self.enableADC2)
        self.tabWidget.addTab(self.set, "")
        self.measure = QtWidgets.QWidget()
        self.measure.setObjectName("measure")
        self.tabWidget.addTab(self.measure, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.widget)
        self.Buttons = QtWidgets.QWidget(self.Electrode)
        self.Buttons.setMinimumSize(QtCore.QSize(200, 170))
        self.Buttons.setMaximumSize(QtCore.QSize(200, 200))
        self.Buttons.setObjectName("Buttons")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Buttons)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bRE = QtWidgets.QPushButton(self.Buttons)
        self.bRE.setMinimumSize(QtCore.QSize(140, 40))
        self.bRE.setMaximumSize(QtCore.QSize(140, 40))
        self.bRE.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bRE.setObjectName("bRE")
        self.verticalLayout_3.addWidget(self.bRE, 0, QtCore.Qt.AlignHCenter)
        self.WEs = QtWidgets.QWidget(self.Buttons)
        self.WEs.setMaximumSize(QtCore.QSize(16777215, 80))
        self.WEs.setObjectName("WEs")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.WEs)
        self.horizontalLayout_3.setContentsMargins(10, 0, 9, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bWE1 = QtWidgets.QPushButton(self.WEs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bWE1.sizePolicy().hasHeightForWidth())
        self.bWE1.setSizePolicy(sizePolicy)
        self.bWE1.setMinimumSize(QtCore.QSize(50, 80))
        self.bWE1.setMaximumSize(QtCore.QSize(60, 80))
        self.bWE1.setObjectName("bWE1")
        self.horizontalLayout_3.addWidget(self.bWE1)
        self.bWE2 = QtWidgets.QPushButton(self.WEs)
        self.bWE2.setMinimumSize(QtCore.QSize(50, 80))
        self.bWE2.setMaximumSize(QtCore.QSize(60, 80))
        self.bWE2.setObjectName("bWE2")
        self.horizontalLayout_3.addWidget(self.bWE2)
        self.verticalLayout_3.addWidget(self.WEs)
        self.bCE = QtWidgets.QPushButton(self.Buttons)
        self.bCE.setMinimumSize(QtCore.QSize(140, 40))
        self.bCE.setMaximumSize(QtCore.QSize(400, 40))
        self.bCE.setObjectName("bCE")
        self.verticalLayout_3.addWidget(self.bCE, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.Buttons, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.Electrode)
        self.plots = QtWidgets.QWidget(self.Content)
        self.plots.setObjectName("plots")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.plots)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.plot1_layout = QtWidgets.QWidget(self.plots)
        self.plot1_layout.setMinimumSize(QtCore.QSize(0, 190))
        self.plot1_layout.setMaximumSize(QtCore.QSize(16777215, 190))
        self.plot1_layout.setObjectName("plot1_layout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.plot1_layout)
        self.horizontalLayout_4.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_6 = QtWidgets.QWidget(self.plot1_layout)
        self.widget_6.setMinimumSize(QtCore.QSize(80, 0))
        self.widget_6.setMaximumSize(QtCore.QSize(80, 16777215))
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(8)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.setymax = QtWidgets.QWidget(self.widget_6)
        self.setymax.setMaximumSize(QtCore.QSize(16777215, 50))
        self.setymax.setObjectName("setymax")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.setymax)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.setymax)
        self.label_11.setMaximumSize(QtCore.QSize(80, 15))
        self.label_11.setObjectName("label_11")
        self.verticalLayout_9.addWidget(self.label_11)
        self.leYMax1 = QtWidgets.QLineEdit(self.setymax)
        self.leYMax1.setObjectName("leYMax1")
        self.verticalLayout_9.addWidget(self.leYMax1)
        self.verticalLayout_8.addWidget(self.setymax)
        self.pbAutoScale1 = QtWidgets.QPushButton(self.widget_6)
        self.pbAutoScale1.setObjectName("pbAutoScale1")
        self.verticalLayout_8.addWidget(self.pbAutoScale1)
        self.pbSetDisplay1 = QtWidgets.QPushButton(self.widget_6)
        self.pbSetDisplay1.setObjectName("pbSetDisplay1")
        self.verticalLayout_8.addWidget(self.pbSetDisplay1)
        self.setymin = QtWidgets.QWidget(self.widget_6)
        self.setymin.setMaximumSize(QtCore.QSize(16777215, 50))
        self.setymin.setObjectName("setymin")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.setymin)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.setymin)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_12.setObjectName("label_12")
        self.verticalLayout_10.addWidget(self.label_12)
        self.leYMin1 = QtWidgets.QLineEdit(self.setymin)
        self.leYMin1.setObjectName("leYMin1")
        self.verticalLayout_10.addWidget(self.leYMin1)
        self.verticalLayout_8.addWidget(self.setymin)
        self.horizontalLayout_4.addWidget(self.widget_6)
        self.plot1 = QtWidgets.QGraphicsView(self.plot1_layout)
        self.plot1.setMinimumSize(QtCore.QSize(0, 185))
        self.plot1.setMaximumSize(QtCore.QSize(16777215, 185))
        self.plot1.setObjectName("plot1")
        self.horizontalLayout_4.addWidget(self.plot1)
        self.verticalLayout_4.addWidget(self.plot1_layout)
        self.plot2_layout = QtWidgets.QWidget(self.plots)
        self.plot2_layout.setMinimumSize(QtCore.QSize(0, 190))
        self.plot2_layout.setMaximumSize(QtCore.QSize(16777215, 190))
        self.plot2_layout.setObjectName("plot2_layout")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.plot2_layout)
        self.horizontalLayout_21.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.widget_7 = QtWidgets.QWidget(self.plot2_layout)
        self.widget_7.setMinimumSize(QtCore.QSize(80, 0))
        self.widget_7.setMaximumSize(QtCore.QSize(80, 16777215))
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(8)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.setymax_2 = QtWidgets.QWidget(self.widget_7)
        self.setymax_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.setymax_2.setObjectName("setymax_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.setymax_2)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_13 = QtWidgets.QLabel(self.setymax_2)
        self.label_13.setMaximumSize(QtCore.QSize(80, 15))
        self.label_13.setObjectName("label_13")
        self.verticalLayout_12.addWidget(self.label_13)
        self.leYMax2 = QtWidgets.QLineEdit(self.setymax_2)
        self.leYMax2.setObjectName("leYMax2")
        self.verticalLayout_12.addWidget(self.leYMax2)
        self.verticalLayout_11.addWidget(self.setymax_2)
        self.pbAutoScale2 = QtWidgets.QPushButton(self.widget_7)
        self.pbAutoScale2.setObjectName("pbAutoScale2")
        self.verticalLayout_11.addWidget(self.pbAutoScale2)
        self.pbSetDisplay2 = QtWidgets.QPushButton(self.widget_7)
        self.pbSetDisplay2.setObjectName("pbSetDisplay2")
        self.verticalLayout_11.addWidget(self.pbSetDisplay2)
        self.setymin_2 = QtWidgets.QWidget(self.widget_7)
        self.setymin_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.setymin_2.setObjectName("setymin_2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.setymin_2)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.setymin_2)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_14.setObjectName("label_14")
        self.verticalLayout_13.addWidget(self.label_14)
        self.leYMin2 = QtWidgets.QLineEdit(self.setymin_2)
        self.leYMin2.setObjectName("leYMin2")
        self.verticalLayout_13.addWidget(self.leYMin2)
        self.verticalLayout_11.addWidget(self.setymin_2)
        self.horizontalLayout_21.addWidget(self.widget_7)
        self.plot2 = QtWidgets.QGraphicsView(self.plot2_layout)
        self.plot2.setMinimumSize(QtCore.QSize(0, 185))
        self.plot2.setMaximumSize(QtCore.QSize(16777215, 185))
        self.plot2.setObjectName("plot2")
        self.horizontalLayout_21.addWidget(self.plot2)
        self.verticalLayout_4.addWidget(self.plot2_layout)
        self.widget_4 = QtWidgets.QWidget(self.plots)
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_14.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.logWindow = QtWidgets.QPlainTextEdit(self.widget_4)
        self.logWindow.setReadOnly(True)
        self.logWindow.setObjectName("logWindow")
        self.verticalLayout_14.addWidget(self.logWindow)
        self.plot2_layout.raise_()
        self.logWindow.raise_()
        self.verticalLayout_4.addWidget(self.widget_4)
        self.horizontalLayout_2.addWidget(self.plots)
        self.verticalLayout_2.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "BioEE Colony Stimulation Platform"))
        self.label_2.setText(_translate("MainWindow", "General Status: "))
        self.label_3.setText(_translate("MainWindow", "Reference:"))
        self.label_4.setText(_translate("MainWindow", "Counter:"))
        self.label_6.setText(_translate("MainWindow", "Working1:"))
        self.label_5.setText(_translate("MainWindow", "Working2:"))
        self.label_7.setText(_translate("MainWindow", "Extra1:"))
        self.label_8.setText(_translate("MainWindow", "Extra2:"))
        self.label_9.setText(_translate("MainWindow", "Extra3:"))
        self.label_10.setText(_translate("MainWindow", "Extra4:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.read), _translate("MainWindow", "Read"))
        self.pbSetRE.setText(_translate("MainWindow", "Set RE"))
        self.pbSetWE1.setText(_translate("MainWindow", "Set WE1"))
        self.pbSetWE2.setText(_translate("MainWindow", "Set WE2"))
        self.pbSwWe1.setText(_translate("MainWindow", "SW_WE1"))
        self.pbSwWe2.setText(_translate("MainWindow", "SW_WE2"))
        self.pbSwEx1.setText(_translate("MainWindow", "SW_EX1"))
        self.pbSwEx2.setText(_translate("MainWindow", "SW_EX2"))
        self.pbEnADC5.setText(_translate("MainWindow", "EN_ADC5"))
        self.pbEnADC6.setText(_translate("MainWindow", "EN_ADC6"))
        self.pbEnADC7.setText(_translate("MainWindow", "EN_ADC7"))
        self.pbEnADC8.setText(_translate("MainWindow", "EN_ADC8"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.set), _translate("MainWindow", "Set"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.measure), _translate("MainWindow", "Measure"))
        self.bRE.setText(_translate("MainWindow", "RE"))
        self.bWE1.setText(_translate("MainWindow", "WE1"))
        self.bWE2.setText(_translate("MainWindow", "WE2"))
        self.bCE.setText(_translate("MainWindow", "CE"))
        self.label_11.setText(_translate("MainWindow", "Y Max"))
        self.pbAutoScale1.setText(_translate("MainWindow", "Auto Scale"))
        self.pbSetDisplay1.setText(_translate("MainWindow", "Set Display"))
        self.label_12.setText(_translate("MainWindow", "Y Min"))
        self.label_13.setText(_translate("MainWindow", "Y Max"))
        self.pbAutoScale2.setText(_translate("MainWindow", "Auto Scale"))
        self.pbSetDisplay2.setText(_translate("MainWindow", "Set Display"))
        self.label_14.setText(_translate("MainWindow", "Y Min"))

