import math
import time

import OpalKelly
import LogManager
import Constants

# Alias to singletons
ok = OpalKelly.Instance()
log = LogManager.Instance()

class CostiFPGA():

	def __init__(self):
		self.dac1Value = 1.65;
		self.dac2Value = 1.65;
		self.dac3Value = 1.65;
		self.dac4Value = 1.65;

	def reset(self):
		ok.setWireIn(Constants.OK_ADDR_CONTROL, Constants.OK_DATA_RESET)
		ok.updateWireIns()
		time.sleep(0.01)
		ok.setWireIn(Constants.OK_ADDR_CONTROL, Constants.OK_DATA_IDLE)
		ok.updateWireIns()

	def setDac1Value(self, value):
		self.dac1Value = value

	def updateDacs(self):
		dac1Int = math.floor(self.dac1Value / Constants.AVDD * Constants.DAC_MAX_CODE)
		dac2Int = math.floor(self.dac2Value / Constants.AVDD * Constants.DAC_MAX_CODE)
		dac3Int = math.floor(self.dac3Value / Constants.AVDD * Constants.DAC_MAX_CODE)
		dac4Int = math.floor(self.dac4Value / Constants.AVDD * Constants.DAC_MAX_CODE)
		
		# Initialize the byte transfer buffer
		dacDataBuffer = bytearray(6)
		dacDataBuffer[0] = int(dac1Int / 16)
		dacDataBuffer[1] = int(dac3Int / 16)
		dacDataBuffer[2] = int(dac1Int % 16) * 16 + int(dac2Int / 256)
		dacDataBuffer[3] = int(dac3Int % 16) * 16 + int(dac4Int / 256)
		dacDataBuffer[4] = int(dac2Int % 256)
		dacDataBuffer[5] = int(dac4Int % 256)

		print(str(dacDataBuffer[0]) + ' ' + str(dacDataBuffer[2]) + ' ' + str(dacDataBuffer[4]))

		# Sending the buffer through pipe in
		log.write("Sending DAC data, and waiting for hardware acknowledgement ...")
		ok.writeToPipeIn(Constants.OK_ADDR_PIPEIN_DAC, dacDataBuffer)

		# Waiting for acknowledgement
		dac1ack = False
		dac2ack = False
		for i in range(Constants.TRIGGER_BACK_CYCLE):
			ok.updateTriggerOuts()
			if ok.isTriggered(Constants.OK_ADDR_TRIGOUT, Constants.OK_BIT_DAC1_ACK_DATA):
				dac1ack = True
			if ok.isTriggered(Constants.OK_ADDR_TRIGOUT, Constants.OK_BIT_DAC2_ACK_DATA):
				dac2ack = True
			if dac1ack and dac2ack:
				log.write("Acknowledgement received from DACs after " + str(i) + " cycles, setting the output ...")
				break

		if ( not dac1ack ) or ( not dac2ack ):
			if dac1ack:
				log.write("Failed to receive acknowledgement from DAC2, write action aborted.")
			elif dac2ack:
				log.write("Failed to receive acknowledgement from DAC1, write action aborted.")
			else :
				log.write("Failed to receive acknowledgement from both DACs, write action aborted.")
			return

		ok.activateTriggerIn(Constants.OK_ADDR_TRIGIN, 0x01)
		
		dac1ack = False
		dac2ack = False
		for i in range(Constants.TRIGGER_BACK_CYCLE):
			ok.updateTriggerOuts()
			if ok.isTriggered(Constants.OK_ADDR_TRIGOUT, Constants.OK_BIT_DAC1_ACK_SET):
				dac1ack = True
			if ok.isTriggered(Constants.OK_ADDR_TRIGOUT, Constants.OK_BIT_DAC2_ACK_SET):
				dac2ack = True
			if dac1ack and dac2ack:
				log.write("Acknowledgement received from DACs after " + str(i) + " cycles, values updated to the outputs: DAC1 = " + 
						str(self.dac1Value) + " , DAC2 = " + str(self.dac2Value) + " , DAC3 = " + str(self.dac3Value) + " , DAC4 = " + str(self.dac4Value))
				break

		if ( not dac1ack ) or ( not dac2ack ):
			if dac1ack:
				log.write("Failed to receive acknowledgement from DAC2, set action aborted.")
			elif dac2ack:
				log.write("Failed to receive acknowledgement from DAC1, set action aborted.")
			else :
				log.write("Failed to receive acknowledgement from both DACs, set action aborted.")
			return

	def setDac2Value():
		pass

	def getADCData():
		pass
