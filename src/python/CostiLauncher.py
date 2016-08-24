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
import LogManager 
import Constants
import CostiFPGA

from DataAcquireThread import DataAcquireThread

# Finding the gui file (python version)
ui_path = utils.feFindDir('ui',4) + '/bioeecosti_ui.py'
gui = imp.load_source('Ui_MainWindow', ui_path)

# Nickname for the singleton CostiFPGA
fpga = CostiFPGA.Instance()
log = LogManager.Instance()

class Costi(QtWidgets.QMainWindow):

  def __init__(self, parent=None):
    ''' Initialization function of the class
        Binding the GUI to the corresponding logic implemented in this class
    '''
    QtWidgets.QWidget.__init__(self, parent)

    # Read UI from Qt Creator
    self.ui = gui.Ui_MainWindow()
    log.write("Initializing GUI ...")

    # Control variables
    self.initializeUI()
    self.ui.setupUi(self)

    # Add status bar into the logging system
    log.addLogMethod(self.ui.statusbar.showMessage, 0)
    
    self.linkGUI()

    # Connect ot hardware (Opal Kelly XEM3010)
    self.connectCostiFPGA()

    # Print additional information
    log.write("GUI initialization finished.")
    if fpga.isDeviceConnected():
      log.write("Welcome to Colony Stimulation Platform @ Bioelectronic Systems Lab.")
    else :
      log.write("Opal Kelly device was not connected successfully, please connect manually.")

  def connectCostiFPGA(self):
    fpga.openDevice()
    log.write("Connecting Opal Kelly device ...")
    if not fpga.isDeviceConnected():
      log.write("Connection failed.")
    else :
      log.write("Successfully connected to Opal Kelly.")
      pllFrequency = fpga.configurePLL()
      log.write("PLL Frequency = " + str(pllFrequency))

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
    '''
    self.ui.action_Load_FPGA.triggered.connect(self.loadBitFile)
    self.ui.action_Connect_FPGA.triggered.connect(self.connectCostiFPGA)

    self.ui.pbSetRE.clicked.connect(self.tryUpdateDAC)
    self.ui.pbSetWE1.clicked.connect(self.tryConfigureADC)

  def loadBitFile(self):
    ''' Load the corresponding bit file to the device (FPGA, Opal Kelly 3010),
        by open a new dialog to find the bit file needed to be read into the GUI
    '''
    fileFinder = QtGui.QFileDialog(self)
    filename = fileFinder.getOpenFileName()
    self.filename = filename[0]
    if (self.filename[-3:] != 'bit'):
      log.write("WARNING: This is probably not a proper bit file for FPGA configuration")

    if fpga.isDeviceConnected() :
      log.write("Loading bit file " + self.filename)
      fpga.loadFile(self.filename.encode('ascii', 'ignore'))
      
      # Device should be configured correctly now, so reset is possible
      log.write("Resetting hardware ...")
      fpga.reset()
      log.write("Reset completed!")
    else :
      log.write("No Opal Kelly device connected. Bit file loading aborted.")

  def tryUpdateDAC(self):
    fpga.updateDacs()

  def tryConfigureADC(self):
    fpga.configureADC()
    fpga.startADCDataStreamThread()

  def closeEvent(self, event):
    ''' Override function
        Re-define what to do at user hit quitting the GUI
    '''
    print("Killing auto-updating threads ...")
    log.write("Killing auto-updating threads ...")
    fpga.stopADCDataStreamThread()
    print("Closing the connection to the Opal Kelly ...")
    log.write("Closing the connection to the Opal Kelly ...")
    # Wait for the opal kelly components to clean itself properly
    # Otherwise core dump is likely to be raised
    time.sleep(1.1)
    event.accept()
