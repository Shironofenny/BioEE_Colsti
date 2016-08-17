#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from CostiLauncher import Costi
from PyQt5 import QtCore, QtWidgets, QtGui

import LogManager
import Constants
import FeUtils as utils

if __name__ == "__main__":
	logFile = utils.LogFile(Constants.LOG_FILE_NAME, 'w')
	LogManager.Instance().addLogMethod(logFile.writeLog, 1)
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle("fusion")
	myapp = Costi()
	myapp.show()
	result = app.exec_()

	# Wait for the opal kelly components to clean itself properly
	# Otherwise core dump is likely to be raised
	#time.sleep(0.1)

	sys.exit(result)

