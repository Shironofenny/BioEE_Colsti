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
from OpalKelly import OpalKelly
from LogManager import LogManager
import Constants

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

        # Link the Opal Kelly FPGA
        self.device = OpalKelly()

        # Local log manager
        self.log = LogManager()

        # Control variables
        self.updateFlag = True
        self.iterateFlag = False
        self.displayNumber = 1

        # Initialize quick access to gui items
        self.bChannel = [None]*48
        self.ledChannel = [None]*48

        self.initializeUI()
        self.ui.setupUi(self)

        self.device.openDevice()
        self.device.configurePLL()

        self.linkGUI()

        # Configure log manager
        self.log.setFileLog(Constants.LOG_FILE_NAME)
        self.log.setQTextLog(self.ui.logWindow)

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
        self.ui.logWindow.setReadOnly(True)

    def configureDisplays(self):
        ''' Configure the options for displaying the data
        self.ui.display1.setMouseEnabled(x=True, y=False)
        self.ui.display2.setMouseEnabled(x=True, y=False)
        '''

    def bondButtons(self):
        ''' Bond all the buttons of the GUI to their corresponding logic
        for i in range(48):
            # Save quick access to all the buttons since this is the first access to them
            self.bChannel[i] = getattr(self.ui, 'channel_sel_'+str(i+1))
            self.bChannel[i].clicked.connect(partial(self.respondChannelClick, i+1))

        self.ui.findFile.clicked.connect(self.findBitFile)
        self.ui.loadFile.clicked.connect(self.loadBitFile)
        '''

    def findBitFile(self):
        ''' Open a new dialog to find the bit file needed to be read into the gui
        '''
        fileFinder = QtGui.QFileDialog(self)
        filename = fileFinder.getOpenFileName()
        self.filename = filename[0]
        if (self.filename[-3:] != 'bit'):
            self.log.write("WARNING: This is probably not a proper bit file for FPGA configuration")
        self.ui.fileName.setText(self.filename)

    def loadBitFile(self):
        ''' Load the corresponding bit file to the device (FPGA, Opal Kelly 6010)
        '''
        self.filename = self.ui.fileName.text().encode('ascii','ignore')
        if (os.path.isfile(self.filename)):
            self.log.write("Loading bit file " + self.filename)
            self.device.loadFile(self.filename)
            self.log.write("Reset FPGA and the ECC chip...")
            self.device.reset()
            self.log.write("Reset completed!")
        else :
            self.log.write("ERROR: FPGA bit file not found")


    def respondChannelClick(self, channelNumber):
        ''' Respond to channel clicks
            Argument channelNumber: the number of the channel. For test channels, it is 38+i, and for extra channels, it is 46+i
        self.log.write("Channel " + str(channelNumber) + " selected...")
        self.device.tryDisplay1()
        '''

    def closeEvent(self, event):
        ''' Override function
            Re-define what to do at user hit quitting the GUI
        '''
        print("Killing auto-updating threads ...")
        self.log.write("Killing auto-updating threads ...", 2)
        self.updateFlag = False
        print("Closing the connection to the Opal Kelly ...")
        self.log.write("Closing the connection to the Opal Kelly ...", 2)
        # Wait for the opal kelly components to clean itself properly
        # Otherwise core dump is likely to be raised
        time.sleep(1.1)
        event.accept()
