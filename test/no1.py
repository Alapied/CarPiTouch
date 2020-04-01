#Import Libraries
import RPi.GPIO as GPIO
import time
import os


from startmain import DebugInfo
from startmain import DebugWarn
from startmain import DebugErr

import datetime
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)

gpioname=37
GPIO.setwarnings(False)

def gpioset():
	#Set up GPIO PIN 
	GPIO.setmode(GPIO.BOARD)
	#Set Pin 13 as input for shutdown ingition switch
	GPIO.setup(gpioname, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	print(str(datetime.datetime.now()) + ' Shutdown GPIO pin configured') 
	


def shutdown():
	print(str(datetime.datetime.now()) + ' Shutdown called') 


if __name__ == '__main__':
	gpioset()
	if (GPIO.input(gpioname) ==1):
		print(str(datetime.datetime.now()) + DebugInfo + 'Ignition state detected')
	else:
		print(str(datetime.datetime.now()) + DebugErr + 'Ignition state inactive yet pi is on')
	
	while True:
		if (GPIO.input(gpioname) ==0):
			max_limit = 5 # Seconds.
			start = time.time()
			while time.time() - start < max_limit:
				if (GPIO.input(gpioname) ==1):
					Ignon = True
					print(str(datetime.datetime.now()) + DebugInfo + 'Ignition on')
				else:
					Ignon = False
			if Ignon == False:
				print(str(datetime.datetime.now()) + DebugInfo + 'Ignition off')
				shutdown()
				break
			


	
	
