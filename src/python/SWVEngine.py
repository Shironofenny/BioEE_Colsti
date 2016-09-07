#! /usr/bin/env python
# -*- coding: utf-8 -*-

import LogManager
import CostiFPGA
import threading
from enum import Enum, unique

log = LogManager.In
fpga = CostiFPGA.Instance()

@unique
class SWVState(Enum):
    Rising=1
    Falling=2

class SWVEngine(object):


    def __init__(self):
        log.write("SWV Engine initializing")
        self.swvEngineThread = threading.Thread(target=self.swvEngine)
        self.stopSWVEngine = threading.Event()

    # ---------------------------------------------------------
    # The following functions are related updating the fpga to
    # perform an swv measurement from a separate thread
    # ---------------------------------------------------------
    def swvEngine(self):

        pass

    def startSWVEngineThread(self):
        if not self.swvEngineThread.isAlive():
          self.swvEngineThread = threading.Thread(target = self.swvEngine)

        try :
          self.swvEngineThread.start()
        except RuntimeError as e:
          log.write("Runtime Error: ({0}): {1}".format(e.errno, e.strerror))
        else :
          self.stopSWVEngine.clear()

    def stopSWVEngineThread(self):
        self.stopSWVEngine.set()
        log.write("Terminating thread name swvEngine")
