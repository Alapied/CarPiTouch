#Import Libraries
import RPi.GPIO as GPIO
import time
import datetime
import os
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
from startmain import DebugInfo
from startmain import DebugWarn
from startmain import DebugErr
print(str(datetime.datetime.now()) + DebugInfo + 'Successfully Imported libaries') #Debug 1
GPIO.setwarnings(False)
gpiopin=36

def SETGPIO():
	#Set up GPIO PIN 
	GPIO.setmode(GPIO.BOARD)
	#Set Pin 11 as input for camera switch
	GPIO.setup(gpiopin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)	
	print(str(datetime.datetime.now()) + DebugInfo + 'Switch GPIO pin configured') #Debug 1
    


	
if __name__ == "__main__":
	# stuff only to run when not called via 'import' here
	SETGPIO()
	while True:
		
		#var1 = True
		
		if (GPIO.input(gpiopin) ==1): ##This will happen if var1 == true
			print(str(datetime.datetime.now()) + DebugInfo + 'Detected Input from Pin 11 Enabling Reversing Camera')
			while (GPIO.input(gpiopin) ==1):
				print(str(datetime.datetime.now()) + DebugInfo +"Pin11 act")
				
			
			


