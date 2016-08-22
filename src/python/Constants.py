#! /usr/bin/env python
# -*- coding: utf-8 -*-

# This file is for the storage of constants

# This part is for constants related to Opal Kelly

from OKByte import OKByte16

# -------------------------------------------------------------------
# Below are constant configurations for genenral software requirement
# -------------------------------------------------------------------

# The name of the logfile
LOG_FILE_NAME = 'costi_runtime.log'

# The AVDD voltage of the analog domain
AVDD = 3.3

# The number of total codes that DAC supports (2^bits)
DAC_MAX_CODE = 4095

# Maximum waiting cycles for trigger outs
TRIGGER_BACK_CYCLE = 50

# -------------------------------------------------------
# Below are constant configurations for costi_bitfile.bit
# -------------------------------------------------------

# Address for communication using opal kelly
OK_ADDR_CONTROL = 0x00

OK_ADDR_WIREOUT = 0x20

OK_ADDR_TRIGIN = 0x40
OK_ADDR_TRIGOUT = 0x60

OK_ADDR_PIPEIN_ADC = 0x80
OK_ADDR_PIPEIN_DAC = 0x81
OK_ADDR_PIPEOUT = 0xA0

# Bit masks for triggers
OK_BIT_DAC1_ACK_DATA = 0x01
OK_BIT_DAC1_ACK_SET = 0x02
OK_BIT_DAC2_ACK_DATA = 0x04
OK_BIT_DAC2_ACK_SET = 0x08

OK_BIT_CTRL_UPDATE = 0x00
OK_BIT_DAC1_SET = 0x02
OK_BIT_DAC2_SET = 0x04

# Corresponding data:
# Data for wirein, control 0
OK_DATA_IDLE = 0x0000
OK_DATA_RESET = 0x8000
OK_DATA_WIN_CTRL0_DACENABLE = 0x0080
OK_DATA_WIN_CTRL0_NULL = 0x0000

# Data for pipein, ADC
OK_DATA_PIN_ADC_DIN = 0x0001
OK_DATA_PIN_ADC_NCS = 0x0002
OK_DATA_PIN_ADC_BEGIN = 0x0004

# Basic bit configuration
BIT = OKByte16(16)
BIT[0] = 0x0001
BIT[1] = 0x0002
BIT[2] = 0x0004
BIT[3] = 0x0008
BIT[4] = 0x0010
BIT[5] = 0x0020
BIT[6] = 0x0040
BIT[7] = 0x0080
BIT[8] = 0x0100
BIT[9] = 0x0200
BIT[10]= 0x0400
BIT[11]= 0x0800
BIT[12]= 0x1000
BIT[13]= 0x2000
BIT[14]= 0x4000
BIT[15]= 0x8000

# This part is related to constants defining the position of all control bits:

# Default value for all control signals
TIA_FB_UNITY		= 0
TIA_FB_5P				= 0
TIA_FB_1P				= 1
TIA_FB_500F			= 0
TIA_FB_250F			= 0
TIA_FB_10M			= 1
TIA_FB_1M				= 1
TIA_FB_100K			= 0
TIA_FB_10K			= 0
TIA_COMP_CAPBYP	= 0
TIA_COMP_RESBYP	= 0
TIA_COMP_CAP1		= 0
TIA_COMP_CAP2		= 0
TIA_COMP_100K		= 0
TIA_COMP_10K 		= 0
TIA_VCM					= 1
TIA_OTATEST			= 0
TIA_CELLTEST 		= 0
TIA_WE 				  = 1
CA_COMP_CAP			= 1
CA_COMP_10K			= 1
CA_COMP_1K 			= 0
CA_COMP_100 		= 0
CA_RESBYP				= 0
CA_CESETEXT			= 0
CA_CEINT				= 1
CA_CEEXT 				= 0
CA_UNITY				= 0
CA_REEXT 				= 1
CA_REINT				= 0

# Set the control signal values using external configuration file
# PFN

# Assemble the control bits into a vector
OK_CTRLVEC1 = CA_COMP_CAP 		* BIT[0]  + CA_COMP_10K 		* BIT[1]  	+ CA_COMP_1K 		* BIT[2]  	+ CA_COMP_100 	 	* BIT[3]  + \
							CA_RESBYP 			*	BIT[4]  + CA_CESETEXT 		* BIT[5]  	+ CA_CEINT 	 		* BIT[6]  	+ CA_CEEXT 				* BIT[7]  + \
							CA_UNITY 				* BIT[8]  + CA_REEXT		 		* BIT[9]  	+ CA_REINT 			* BIT[10] 	+ TIA_WE 					* BIT[11] + \
							TIA_CELLTEST		* BIT[12] + TIA_OTATEST 		* BIT[13] 	+ TIA_VCM 			* BIT[14] 	+ TIA_FB_10K   		* BIT[15]

OK_CTRLVEC2 = TIA_COMP_100K 	* BIT[0]	 + TIA_COMP_CAP1 	* BIT[1] 	+ TIA_COMP_CAP2 * BIT[2] 	+ TIA_COMP_RESBYP * BIT[3] + \
							TIA_COMP_CAPBYP * BIT[4]	 + TIA_FB_10K 		* BIT[5] 	+ TIA_FB_100K 	* BIT[6] 	+ TIA_FB_1M 			* BIT[7] + \
							TIA_FB_10M 			* BIT[8]	 + TIA_FB_250F 		* BIT[9] 	+ TIA_FB_500F 	* BIT[10] + TIA_FB_1P 			* BIT[11] + \
							TIA_FB_5P 			* BIT[12]  + TIA_FB_UNITY 	* BIT[13]

OK_CHANNELMAP = [[1, 4], [1, 3], [1, 2], [1, 6], [1, 5], [1, 7],
								 [0, 3], [0, 4], [0, 0], [0, 5], [0, 2], [0, 6], [0, 1], [0, 7],
								 [4, 3], [4, 2], [4, 0], [4, 4], [4, 5], [4, 1], [4, 7], [4, 6],
								 [3, 3], [3, 5], [3, 2], [3, 0], [3, 4], [3, 7], [3, 1], 
								 [2, 3], [2, 5], [2, 0], [2, 7], [2, 2], 
								 [3, 6],
								 [2, 1], [2, 6], [2, 4],
								 [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7],
								 [1, 0], [1, 1]]

OK_ADC_VEC = OKByte16(104)

ADC_WRITE 		= 1
ADC_REPEAT 		= 1
ADC_AIN0 			= 1
ADC_AIN1 			= 1
ADC_AIN2 			= 1
ADC_AIN3 			= 1
ADC_AIN4 			= 1
ADC_AIN5 			= 1
ADC_AIN6 			= 1
ADC_AIN7 			= 1
ADC_TSENSE 		= 1
ADC_DONTCARE1 = 0
ADC_DONTCARE2 = 0
ADC_EXTREF 		= 1
ADC_TMPAVG 		= 0
ADC_STANDBY 	= 0
ADC_AIN1 			= 1

OK_ADC_BIT_VEC = CA_COMP_CAP 		* BIT[0]  + CA_COMP_10K 		* BIT[1]  	+ CA_COMP_1K 		* BIT[2]  	+ CA_COMP_100 	 	* BIT[3]  + \
							CA_RESBYP 			*	BIT[4]  + CA_CESETEXT 		* BIT[5]  	+ CA_CEINT 	 		* BIT[6]  	+ CA_CEEXT 				* BIT[7]  + \
							CA_UNITY 				* BIT[8]  + CA_REEXT		 		* BIT[9]  	+ CA_REINT 			* BIT[10] 	+ TIA_WE 					* BIT[11] + \
							TIA_CELLTEST		* BIT[12] + TIA_OTATEST 		* BIT[13] 	+ TIA_VCM 			* BIT[14] 	+ TIA_FB_10K   		* BIT[15]
