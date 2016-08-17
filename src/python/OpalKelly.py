import imp
import sys
import os
import time

import FeUtils as utils

source_path = utils.feFindDir('lib',3)
if not source_path :
		# Exit the program when no library could found
		print('Library path not found, please check if library files exist')
		sys.exit(1)

source_path = source_path + '/ok/ok.py';

# Load library for Opal Kelly (ok)
ok = imp.load_source('ok', source_path)

# User defined modules
import Constants

# Few lines to make it a (dirty) singleton
# If you want to use LogManager in a singleton way, then the correct call would be:
# LogManager.Instance().methodToCall(args)

_instance = None

def Instance():
	global _instance
	if _instance is None:
		_instance = OpalKelly();
	return _instance

class OpalKelly:
	
	def __init__(self):
		self.xem = ok.okCFrontPanel()
		self.pll = ok.PLL22393()
		self.activationFlag = False

	def openDevice(self):
		errormsg = self.xem.OpenBySerial("")
		if (self.xem.NoError == errormsg):
				self.activationFlag = True
		return errormsg

	def configurePLL(self):
		if (self.activationFlag):
				self.xem.GetPLL22393Configuration(self.pll)
				self.pll.SetReference(48.0)
				self.pll.SetPLLParameters(0, 400, 48, True)
				self.pll.SetOutputSource(0, ok.PLL22393.ClkSrc_PLL0_0)
				self.pll.SetOutputDivider(0, 4)
				self.pll.SetOutputEnable(0, True)
				self.xem.SetPLL22393Configuration(self.pll)
				return self.pll.GetPLLFrequency(0)
		else :
				pass

	def loadFile(self, filename):
		if (self.activationFlag):
				output = self.xem.ConfigureFPGA(filename)
		else :
				pass

	def isDeviceConnected(self):
		return self.activationFlag

	def setWireIn(self,addr,data):
			self.xem.SetWireInValue(addr,data)

	def updateWireIns(self):
			self.xem.updateWireIns()

	def activateTriggerIn(self,addr,bit):
			self.xem.ActivateTriggerIn(addr,bit)
