#! /usr/bin/python

#Import Libraries
import RPi.GPIO as GPIO
import time
import os
import datetime
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
from multiprocessing import Pool
import subprocess

no1 = "/home/pi/Desktop/test/no1.py"
no2 = "/home/pi/Desktop/test/no2.py"

GPIO.setwarnings(False)

DebugInfo = ' [Info] '
DebugWarn = ' [Warning] '
DebugErr = ' [Error] '

def run_process(process):                                                             
    os.system('python {}'.format(process))
def setgpio():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


if __name__ == '__main__':
	setgpio()
		
	print(str(datetime.datetime.now()) + DebugInfo +'Starting no 1script')
	print(str(datetime.datetime.now()) + DebugInfo + 'Starting no2 script')
	processes = (no1, no2,)
	pool = Pool(processes=2)
	pool.map(run_process, processes)  
	print("after")
