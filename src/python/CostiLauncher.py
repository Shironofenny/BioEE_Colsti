#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import threading
import imp

from functools import partial

from PyQt5 import QtCore, QtWidgets, QtGui
import pyqtgraph as pg
from pyqtgraph import PlotWidget

import FeUtils as utils
import OpalKelly
import LogManager 
import Constants
from ColstiFPGA import CostiFPGA

# Finding the gui file (python version)
ui_path = utils.feFindDir('ui',4) + '/bioeecosti_ui.py'
gui = imp.load_source('Ui_MainWindow', ui_path)

class Costi(QtWidgets.QMainWindow):

	def __init__(self, parent=None):
		''' Initialization function of the class
				Binding the GUI to the corresponding logic implemented in this class
		'''
		QtWidgets.QWidget.__init__(self, parent)

		# Read UI from Qt Creator
		self.ui = gui.Ui_MainWindow()
		LogManager.Instance().write("Initializing GUI ...")

		# Control variables
		self.initializeUI()
		self.ui.setupUi(self)

		self.linkGUI()

		# Connect ot hardware (Opal Kelly XEM3010)
		self.connectOpalKelly()

		LogManager.Instance().addLogMethod(self.ui.statusbar.showMessage, 0)
		LogManager.Instance().write("GUI initialization finished.")
		if OpalKelly.Instance().isDeviceConnected():
			LogManager.Instance().write("Welcome to Colony Stimulation Platform @ Bioelectronic Systems Lab.")
		else :
			LogManager.Instance().write("Opal Kelly device was not connected successfully, please connect manually.")

		self.device = CostiFPGA()

	def connectOpalKelly(self):
		OpalKelly.Instance().openDevice()
		LogManager.Instance().write("Connecting Opal Kelly device ...")
		if not OpalKelly.Instance().isDeviceConnected():
			LogManager.Instance().write("Connection failed.")
		else :
			LogManager.Instance().write("Successfully connected to Opal Kelly.")
			pllFrequency = OpalKelly.Instance().configurePLL()
			LogManager.Instance().write("PLL Frequency = " + str(pllFrequency))

	def initializeUI(self):
		''' Configure UI options that needs to go before setupUI()
		'''
		# Change options for pyqtgraph
		pg.setConfigOption('background',(239,235,231))
		pg.setConfigOption('foreground','k')

	def linkGUI(self):
		''' Linking GUI element's to their corresponding logic
		'''
		self.bondButtons()
		self.configureDisplays()

	def configureDisplays(self):
		''' Configure the options for displaying the data
		'''
		self.ui.plot1.setMouseEnabled(x=True, y=False)
		self.ui.plot2.setMouseEnabled(x=True, y=False)

	def bondButtons(self):
		''' Bond all the buttons of the GUI to their corresponding logic
		self.ui.findFile.clicked.connect(self.findBitFile)
		self.ui.loadFile.clicked.connect(self.loadBitFile)
		'''
		self.ui.action_Load_FPGA.triggered.connect(self.loadBitFile)
		self.ui.action_Connect_FPGA.triggered.connect(self.connectOpalKelly)

		self.ui.pbSetRE.clicked.connect(self.tryUpdateDAC)

	def loadBitFile(self):
		''' Load the corresponding bit file to the device (FPGA, Opal Kelly 3010),
				by open a new dialog to find the bit file needed to be read into the GUI
		'''
		fileFinder = QtGui.QFileDialog(self)
		filename = fileFinder.getOpenFileName()
		self.filename = filename[0]
		if (self.filename[-3:] != 'bit'):
			LogManager.Instance().write("WARNING: This is probably not a proper bit file for FPGA configuration")

		if OpalKelly.Instance().isDeviceConnected() :
			LogManager.Instance().write("Loading bit file " + self.filename)
			OpalKelly.Instance().loadFile(self.filename.encode('ascii', 'ignore'))
			
			# Device should be configured correctly now, so reset is possible
			LogManager.Instance().write("Resetting hardware ...")
			self.device.reset()
			LogManager.Instance().write("Reset completed!")
		else :
			LogManager.Instance().write("No Opal Kelly device connected. Bit file loading aborted.")

	def tryUpdateDAC(self):
		self.device.updateDacs()

	def closeEvent(self, event):
		''' Override function
				Re-define what to do at user hit quitting the GUI
		'''
		print("Killing auto-updating threads ...")
		LogManager.Instance().write("Killing auto-updating threads ...")
		print("Closing the connection to the Opal Kelly ...")
		LogManager.Instance().write("Closing the connection to the Opal Kelly ...")
		# Wait for the opal kelly components to clean itself properly
		# Otherwise core dump is likely to be raised
		time.sleep(1.1)
		event.accept()
