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

		def setWireIn(self,addr,data):
				self.xem.SetWireInValue(addr,data)

		def updateWireIns(self):
				self.xem.updateWireIns()

		def activateTriggerIn(self,addr,bit):
				self.xem.ActivateTriggerIn(addr,bit)

		def reset(self):
				''' Reset the FPGA 
						Only valid for bitfile_fpga.bit wrote by Daniel Bellin
				'''
				self.xem.SetWireInValue(Constants.OK_ADDR_WIN_CTRL0, Constants.OK_DATA_WIN_CTRL0_RESET)
				self.xem.UpdateWireIns()
				time.sleep(1.0)
				self.xem.SetWireInValue(Constants.OK_ADDR_WIN_CTRL0, Constants.OK_DATA_WIN_CTRL0_NULL)
				self.xem.UpdateWireIns()

		def sendADCSignal(self):
				''' Configure ADC's 
						Only valid for bitfile_fpga.bit wrote by Daniel Bellin
				'''
				self.xem.SetWireInValue()

		def tryConfiguration(self):
				self.xem.SetWireInValue(Constants.OK_ADDR_COMMAND, Constants.OK_STORE_1)
				self.xem.SetWireInValue(Constants.OK_ADDR_DATA, 0x55)
				self.xem.UpdateWireIns()

				self.xem.ActivateTriggerIn(Constants.OK_ADDR_TRIGGER, Constants.OK_DATA_TRIGGER)

				self.xem.SetWireInValue(0x00,0x02)
				self.xem.SetWireInValue(0x01,0x00)
				self.xem.UpdateWireIns()

				self.xem.ActivateTriggerIn(0x40,0x00)

		def tryDisplay1(self):
				self.xem.SetWireInValue(0x00,0x03)
				self.xem.SetWireInValue(0x01,0x01)
				self.xem.UpdateWireIns()
				self.xem.ActivateTriggerIn(0x40,0x00)

		def tryDisplay2(self):
				self.xem.SetWireInValue(0x00,0x03)
				self.xem.SetWireInValue(0x01,0x02)
				self.xem.UpdateWireIns()
				self.xem.ActivateTriggerIn(0x40,0x00)

