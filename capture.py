#! /usr/bin/env python
#coding=utf-8

from VideoCapture import Device
import time

ISOTIMEFORMAT='%Y-%m-%d %X'
while 1:
	cam = Device()
	cam.saveSnapshot('now.jpg')
	time.sleep(10)
	print time.strftime( ISOTIMEFORMAT, time.localtime() )