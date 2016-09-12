#! /usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time

import LogManager
import CostiFPGA
import Constants
from enum import Enum

log = LogManager.Instance()
fpga = CostiFPGA.Instance()

class SWVState(Enum):
    Start = 1
    Rising = 2
    Falling = 3
    End = 4
    Idle = 5

class SWVEngine(object):

    def __init__(self):
        log.write("SWV Engine initializing")
        self.swvEngineThread = threading.Thread(target=self.swvEngine)
        self.stopSWVEngine = threading.Event()

        self.swvState = SWVState.Idle

        self.period = float(0.5/Constants.SWV_DEFAULT_FREQ) # 1/2 1/F
        self.amp = Constants.SWV_DEFAULT_AMP
        self.initE = Constants.SWV_DEFAULT_STARTE
        self.endE = Constants.SWV_DEFAULT_ENDE
        self.incrE = Constants.SWV_DEFAULT_INCRE
        self.initWait = Constants.SWV_DEFAULT_INITWAIT

        self.reValue = Constants.SWV_DEFAULT_WE - self.initE
        self.weValue = Constants.SWV_DEFAULT_WE

        self.control = {SWVState.Start : self.initSWV,
                        SWVState.Rising : self.raiseOutput,
                        SWVState.Falling : self.lowerOutput,
                        SWVState.End : self.endSWV,
                        SWVState.Idle : self.idle}

    # ---------------------------------------------------------
    # The following functions are related updating the fpga to
    # perform an swv measurement from a separate thread
    # ---------------------------------------------------------
    def initSWV(self):
        time.sleep(self.initWait)
        log.write("Initializing SWV, please wait ...")
        log.write("Performing SWV ...")
        self.reValue = Constants.SWV_DEFAULT_WE - self.initE
        fpga.setREValue(self.reValue)
        fpga.setWE1Value(self.weValue)
        fpga.setWE2Value(self.weValue)
        time.sleep(self.initWait)
        self.swvState = SWVState.Rising

    def raiseOutput(self):
        if self.reValue == self.weValue - self.initE :
            self.reValue = self.reValue + self.amp
        else :
            self.reValue = self.reValue + self.amp * 2 - self.incrE

        fpga.setREValue(self.reValue)
        self.swvState = SWVState.Falling

    def lowerOutput(self):
        self.reValue = self.reValue - 2 * self.amp
        fpga.setREValue(self.reValue)

        if self.reValue <= self.weValue - self.endE :
            self.swvState = SWVState.End
        else :
            self.swvState = SWVState.Rising

    def endSWV(self):
        log.write("SWV ends.")
        self.stopSWVEngineThread()
        self.swvState = SWVState.Idle

    def idle(self):
        pass

    def swvEngine(self):
        while not self.stopSWVEngine.wait(self.period):
            self.control[self.swvState]()

    def startSWVEngineThread(self):
        if not self.swvEngineThread.isAlive():
          self.swvEngineThread = threading.Thread(target = self.swvEngine)
        try :
          self.swvEngineThread.start()
        except RuntimeError as e:
          log.write("Runtime Error: ({0}): {1}".format(e.errno, e.strerror))
        else :
          self.stopSWVEngine.clear()
          self.swvState = SWVState.Start

    def stopSWVEngineThread(self):
        self.stopSWVEngine.set()
        log.write("Terminating thread name swvEngine")
