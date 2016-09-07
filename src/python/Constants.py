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
AVDD = 3.3 # in volts

# The number of total codes that DAC supports (2^bits)
DAC_MAX_CODE = 4095

# Maximum waiting cycles for trigger outs
TRIGGER_BACK_CYCLE = 50

# -------------------------------------------------------
# Below are the default voltages of the DAC's
# -------------------------------------------------------

RE_DEFAULT_VOLTAGE = 1.25
WE1_DEFAULT_VOLTAGE = 1.25
WE2_DEFAULT_VOLTAGE = 1.25
ADCREF_DEFAULT_VOLTAGE = 3.3

# -------------------------------------------------------
# Below are constant configurations for thread management
# -------------------------------------------------------

ADC_DATA_CHECK_INTERVAL = 0.001 # in seconds
TRIGGER_OUT_CHECK_INTERVAL = 0.0005 # in seconds
PLOT_REFRESHING_INTERVAL = 0.001 # in seconds
MAIN_UPDATING_INTERVAL = 0.001 # in seconds

# -------------------------------------------------------------
# Below are the default data display and storage configurations
# -------------------------------------------------------------

NUM_DATA_DISPLAY = 1000
DATA_DISP_DOWNSAMPLE = 400
DATA_SAVE_DOWNSAMPLE = 200

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
OK_BIT_DAC1_ACK_DATA = 0x0001
OK_BIT_DAC1_ACK_SET = 0x0002
OK_BIT_DAC2_ACK_DATA = 0x0004
OK_BIT_DAC2_ACK_SET = 0x0008
OK_BIT_ADC_FREQ_EX = 0x0010
OK_BIT_SDRAM_READY = 0x0080

OK_BIT_CTRL_UPDATE = 0x0000
OK_BIT_DAC_SET = 0x0001

# Data for Control signals
OK_DATA_RESET = 0x8000
OK_DATA_IDLE = 0x0000

OK_DATA_SWDEFAULT = 0x0003
OK_DATA_SW = [0x0001, 0x0002, 0x0004, 0x0008]

OK_DATA_ADCDEFAULT = 0x0000

# Pipe out block size
OK_PIPEOUT_BLOCKSIZE = 1024
OK_PIPEOUT_TRANSFERSIZE = 1 * OK_PIPEOUT_BLOCKSIZE
