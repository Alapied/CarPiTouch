#! /usr/bin/python3.7

#Import Libraries
import time
import os
import datetime
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)

navit = "/home/pi/Desktop/CarPiTouch/startnavit.py"

DebugInfo = ' [Info] '
DebugWarn = ' [Warning] '
DebugErr = ' [Error] '
 
def run_Navit():
	time.sleep(3)
	print(str(datetime.datetime.now()) + DebugInfo + 'Marker: Navit Started')
	Navitstatus = os.system('systemctl is-active --quiet navit') # will return 0 for active else inactive
	if Navitstatus == 0:
		print(str(datetime.datetime.now()) + DebugInfo + 'Navit Active')

	else:
		print(str(datetime.datetime.now()) + DebugWarn + 'Navit process not running, Service not started or error has been thrown')
		print(str(datetime.datetime.now()) + DebugInfo + ' Restarting NavIt ') #Debug 1
		os.system('navit')
run_Navit()
