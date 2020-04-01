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
import time
timestr = time.strftime("%Y-%m-%d--%H-%M-%S")

gpioignition=37
gpioRevCheck=11
gpioDashCheck=13

GPIO.setwarnings(False)

#Dashname = "/" + timestr + "-Dashcam"
Revname = "/" + timestr + "-Revcam"

#Dashdest_file = directory + Dashname
#Dashsrc_file = '/home/pi/Frontoutput.avi'
Revdest_file = directory + Revname
Revsrc_file = '/home/pi/output.avi'

def gpioset():
	#Set up GPIO PIN 
	GPIO.setmode(GPIO.BOARD)
	#Set Pin as input for shutdown ingition switch
	GPIO.setup(gpioignition, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	print(str(datetime.datetime.now()) + DebugInfo + 'Ignition GPIO pin configured') 
	GPIO.setup(gpioDashCheck, GPIO.OUT)
	GPIO.setup(gpioRevCheck, GPIO.OUT)
	GPIO.output(gpioRevCheck, GPIO.LOW)
	GPIO.output(gpioDashCheck, GPIO.LOW)
	
def copyoutput():
	#shutil.copy2(Dashsrc_file, Dashdest_file)
	print(str(datetime.datetime.now()) + DebugInfo +'Moving Output files')
	shutil.copy2(Revsrc_file, Revdest_file)
	time.sleep(3)
	#os.remove(Dashsrc_file)
	os.remove(Revsrc_file)
	
def shutdown():
	GPIO.cleanup()
	os.system('sudo shutdown -h now')
	
def stopfeed():
	print(str(datetime.datetime.now()) + DebugInfo + 'Stopping Cam Feeds')
	GPIO.output(gpioDashCheck, GPIO.HIGH)
	GPIO.output(gpioRevCheck, GPIO.HIGH)
	time.sleep(0.5)
if __name__ == '__main__':
	gpioset()
	if (GPIO.input(gpioignition) ==1):
		print(str(datetime.datetime.now()) + DebugInfo + 'Ignition state detected')
	else:
		print(str(datetime.datetime.now()) + DebugErr + 'Ignition state inactive yet pi is on')
	while True:
		if (GPIO.input(gpioignition) ==0):
			max_limit = 5	# Seconds.
			start = time.time()
			while time.time() - start < max_limit:
				if (GPIO.input(gpioignition) ==1):
					Ignon = True
					print(str(datetime.datetime.now()) + DebugInfo + 'Ignition on')
				else:
					Ignon = False
			if Ignon == False:
				print(str(datetime.datetime.now()) + DebugInfo + 'Ignition off')
				stopfeed()
				copyoutput()
				shutdown()
				break
			


	
	
