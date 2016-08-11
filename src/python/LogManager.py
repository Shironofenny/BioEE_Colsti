from PyQt5 import QtCore, QtWidgets, QtGui
import time

class LogManager():

    def __init__(self):
        self.fileLogFlag = False
        self.displayLogFlag = False
        self.logReady = False
        self.fileName = None
        self.logFile = None
        self.logDisplay = None

    def setFileLog(self, filename):
        self.fileName = filename
        self.fileLogFlag = True
        self.logFile = open(self.fileName, 'w')
        if (self.displayLogFlag):
            self.logReady = True

    def setQTextLog(self, qText):
        self.logDisplay = qText
        self.displayLogFlag = True
        if (self.fileLogFlag):
            self.logReady = True

    def isLogReady(self):
        return self.logReady

    def write(self, logStr, level = 1):
        if (level == 1):
            self.logDisplay.appendPlainText(time.strftime("[%H:%M:%S]") + " : " + logStr)
        else :
            pass

        self.logFile.write(time.strftime("[%H:%M:%S]") +" : " + logStr + '\n')

