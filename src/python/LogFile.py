#! /usr/bin/env python
# -*- coding: utf-8 -*-

class LogFile(file):
  # A subclass of file just to have a more convienient way to write logs
  def __init__(self, name, mode = 'r'):
    self = file.__init__(self, name, mode)

  def writeLog(self, string):
    self.write(string + '\n')
