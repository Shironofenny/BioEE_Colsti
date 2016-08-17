from PyQt5 import QtCore, QtWidgets, QtGui
import time

# Few lines to make it a (dirty) singleton
# If you want to use LogManager in a singleton way, then the correct call would be:
# LogManager.Instance().methodToCall(args)

_instance = None

def Instance():
	global _instance
	if _instance is None:
		_instance = LogManager();
	return _instance

class LogManager():

		def __init__(self):
			""" Initialize the empty log function list
			"""
			self.logMethods = []
			self.logPriority = []

		def addLogMethod(self, logMethod, priority):
			""" Add a log method in to the class. 
					The method must take one and only one argument which is the string to be written
			"""
			self.logMethods.append(logMethod)
			self.logPriority.append(priority)
		
		def getLogNumbers(self):
			""" Get the number of log methods currently available in the log manager
			"""
			return len(self.logMethods)

		def write(self, logStr, level = 'all'):
			if (level == 'all'):
				for logMethod in self.logMethods:
					logMethod(time.strftime("[%H:%M:%S]") +" : " + logStr)
			else :
				# Finding all the logmethods registerd with specified priority level, and write those logs
				for index in [i for (i,priority) in enumerate(self.logPriority) if priority in level]:
					self.logMethods[index](time.strftime("[%H:%M:%S]") +" : " + logStr)
