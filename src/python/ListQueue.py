#! /usr/bin/env python
# -*- coding: utf-8 -*-

class ListQueue():
  """ I choose not to subclass list, but do a wrap up of the List class
      simply because there seems to be some controversy on how List, or
      more generally, mutable classes should be inheritted
  """

  def __init__(self, size = None):
    self.dataList = []
    self.maxSize = size

  def push(self, element):
    if self.maxSize == None :
      self.dataList.append(element)
      return None
    else :
      if len(self.dataList) == self.maxSize :
        self.dataList.append(element)
        return self.dataList.pop(0)
      else :
        self.dataList.append(element)
        return None

  def setSize(self, size):
    self.maxSize = size

  def getSize(self):
    return self.maxSize

  def isFull(self):
    return len(self.dataList) >= self.maxSize

  def isEmpty(self):
    return len(self.dataList) == 0

  def getData(self):
    return self.dataList

  def peekLast(self):
    return self.dataList[-1]

