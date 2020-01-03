#Import Libraries
import RPi.GPIO as GPIO
import time
import os

from startmain import directory
from startmain import DebugInfo
from startmain import DebugWarn
from startmain import DebugErr

import shutil #copy paste
import datetime
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)


Dashname = "/" + str(datetime.datetime.now()) + " Dashcam"
Revname = "/" + str(datetime.datetime.now()) + " Revcam"

Dashdest_file = directory + Dashname
Dashsrc_file = '/home/pi/Desktop/CarPiTouch/Frontoutput.avi'
Revdest_file = directory + Revname
Revsrc_file = '/home/pi/Desktop/CarPiTouch/output.avi'

def gpioset():
	#Set up GPIO PIN 
	GPIO.setmode(GPIO.BCM)
	#Set Pin 13 as input for shutdown ingition switch
	GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	print(str(datetime.datetime.now()) + ' Shutdown GPIO pin configured') 
	
def copyoutput():
	shutil.copy2(Dashsrc_file, Dashdest_file)
	print(str(datetime.datetime.now()) + DebugInfo +'Moving Output files')
	shutil.copy2(Revsrc_file, Revdest_file)

def shutdown():
	os.system('sudo shutdown --poweroff')


if __name__ == '__main__':
	gpioset()
	GPIO.input(27) = var1
	if var1:
		print(str(datetime.datetime.now()) + DebugInfo + 'Ignition state detected')
	else:
		print(str(datetime.datetime.now()) + DebugErr + 'Ignition state inactive yet pi is on')
	
	while True:
		GPIO.input(27) = var1
		if not var1:
			max_limit = 5	# Seconds.
			start = time.time()
			while time.time() - start < max_limit:
				GPIO.input(27) = var1
				if var1:
					Ignon = True
					print(str(datetime.datetime.now()) + DebugInfo + 'Ignition on')
				else:
					Ignon = False
			if Ignon == False:
				print(str(datetime.datetime.now()) + DebugInfo + 'Ignition off')
				copyoutput()
				shutdown()
				break
			


	
	
