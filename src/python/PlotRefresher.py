#! /usr/bin/env python
# -*- coding: utf-8 -*-

import threading

import CostiFPGA
import LogManager
import Constants

from ListQueue import ListQueue

# Nickname for the singleton CostiFPGA
fpga = CostiFPGA.Instance()
log = LogManager.Instance()

class PlotRefresher(object) :

  def __init__(self):
    self.plot1Handle = None
    self.plot2Handle = None
    self.plot1Number = 0
    self.plot2Number = 1
    self.plot1YLim = [0,0]
    self.plot2YLim = [0,0]

    # Plot refresher thread control
    self.plotRefresherThread = threading.Thread(target = self.plotRefresher)
    self.stopPlotRefresher = threading.Event()

    # Initialize a maximum of 8 channel's data
    self.channels = [None] * 8
    for i in range(8):
      self.channels[i] = ListQueue(Constants.NUM_DATA_DISPLAY)

    self.channelLock = threading.RLock()

    # Initialize the down sample counter
    self.dispDownsampleCounter = [0] * 8
    self.saveDownsampleCounter = [0] * 8

  def setPlot1Handle(self, plot1):
    self.plot1Handle = plot1

  def setPlot2Handle(self, plot2):
    self.plot2Handle = plot2

  def setPlot1Number(self, number):
    self.plot1Number = number

  def setPlot2Number(self, number):
    self.plot2Number = number

  def setPlot1YLim(self, ymin, ymax):
    pass

  def setPlot2YLim(self, ymin, ymax):
    pass

  def peekWE1Value(self):
    if self.channels[0].isEmpty() :
      return "--"
    else :
      return "{0:.4f}".format(self.channels[0].peekLast())

  def peekWE2Value(self):
    if self.channels[1].isEmpty() :
      return "--"
    else :
      return "{0:.4f}".format(self.channels[1].peekLast())

  def peekCEValue(self):
    if self.channels[2].isEmpty() :
      return "--"
    else :
      return "{0:.4f}".format(self.channels[2].peekLast())

  def peekREValue(self):
    if self.channels[3].isEmpty() :
      return "--"
    else :
      return "{0:.4f}".format(self.channels[3].peekLast())

  def peekExtraValue(self, i):
    if self.channels[i+3].isEmpty() :
      return "--"
    else :
      return "{0:.4f}".format(self.channels[i+3].peekLast())

  def updatePlots(self):
    self.channelLock.acquire()

    if not self.channels[self.plot1Number].isEmpty():
      self.plot1Handle.clear()
      self.plot1Handle.plot(self.channels[self.plot1Number].getData())
      self.plot1Handle.setXRange(0, 1000, padding=0)

    if not self.channels[self.plot2Number].isEmpty():
      self.plot2Handle.clear()
      self.plot2Handle.plot(self.channels[self.plot2Number].getData())
      self.plot2Handle.setXRange(0, 1000, padding=0.02)
      self.plot2Handle.getAxis('bottom').setScale(0.2)
      self.plot2Handle.getAxis('bottom').setLabel('Time', units='s')

    self.channelLock.release()

# ---------------------------------------------------------
# The following functions are related to sorting incoming 
# ADC data into different channels
# ---------------------------------------------------------

  def plotRefresher(self):
    while not self.stopPlotRefresher.wait(Constants.PLOT_REFRESHING_INTERVAL):
      data = fpga.getDataQueueOut()
      if data != None :
        adcRange = fpga.getADCRefValue()
        self.channelLock.acquire()
        for i in range(data.getSize()):
          point = data[i]
          addr = int(point / 4096)
          value = float(point % 4096) / Constants.DAC_MAX_CODE * adcRange
          if addr >= 8 :
            pass
            log.write("Data received for address larger than 4'b0111. This is not handleded by current program")
          else :
            self.dispDownsampleCounter[addr] = self.dispDownsampleCounter[addr] + 1
            if self.dispDownsampleCounter[addr] == Constants.DATA_DISP_DOWNSAMPLE :
              self.dispDownsampleCounter[addr] = 0
              self.channels[addr].push(value)
        self.channelLock.release()

  def startPlotRefresherThread(self):
    if not self.plotRefresherThread.isAlive():
      self.plotRefresherThread = threading.Thread(target = self.plotRefresher)

    try :
      self.plotRefresherThread.start()
    except RuntimeError as e:
      log.write("Runtime Error: ({0}): {1}".format(e.errno, e.strerror))
    else :
      self.stopPlotRefresher.clear()

  def stopPlotRefresherThread(self):
    self.stopPlotRefresher.set()
