#Import Libraries
import RPi.GPIO as GPIO
import time
import os
import Dashcam as DC
import ReverseCam as RC

from startmain import directory
from startmain import DebugInfo
from startmain import DebugWarn
from startmain import DebugErr

import shutil #copy paste
import datetime
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)

gpioname=37
GPIO.setwarnings(False)

Dashname = "/" + str(datetime.datetime.now()) + " Dashcam"
Revname = "/" + str(datetime.datetime.now()) + " Revcam"

Dashdest_file = directory + Dashname
Dashsrc_file = '/home/pi/Desktop/CarPiTouch/Frontoutput.avi'
Revdest_file = directory + Revname
Revsrc_file = '/home/pi/Desktop/CarPiTouch/output.avi'

def gpioset():
	#Set up GPIO PIN 
	GPIO.setmode(GPIO.BOARD)
	#Set Pin as input for shutdown ingition switch
	GPIO.setup(gpioname, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	print(str(datetime.datetime.now()) + 'Ignition GPIO pin configured') 
	
def copyoutput():
	shutil.copy2(Dashsrc_file, Dashdest_file)
	print(str(datetime.datetime.now()) + DebugInfo +'Moving Output files')
	shutil.copy2(Revsrc_file, Revdest_file)

def shutdown():
	os.system('sudo shutdown --poweroff')


if __name__ == '__main__':
	gpioset()
	
	if (GPIO.input(gpioname) ==1):
		print(str(datetime.datetime.now()) + DebugInfo + 'Ignition state detected')
	else:
		print(str(datetime.datetime.now()) + DebugErr + 'Ignition state inactive yet pi is on')
	
	while True:
		
		if (GPIO.input(gpioname) ==0):
			max_limit = 5	# Seconds.
			start = time.time()
			while time.time() - start < max_limit:
				if (GPIO.input(gpioname) ==1):
					Ignon = True
					print(str(datetime.datetime.now()) + DebugInfo + 'Ignition on')
				else:
					Ignon = False
			if Ignon == False:
				print(str(datetime.datetime.now()) + DebugInfo + 'Ignition off')
				copyoutput()
				shutdown()
				break
			


	
	
