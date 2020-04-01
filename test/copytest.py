#Import Libraries
import RPi.GPIO as GPIO
import time
import os
import shutil #copy paste
import datetime
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
import time
timestr = time.strftime("%Y-%m-%d--%H-%M-%S")
print timestr
gpioname=37
GPIO.setwarnings(False)
directory = '/media/pi/6EAA-CEC1/footage'
Dashname = "/" +timestr + "-Dashcam"
Revname = "/" + timestr + "-Revcam"

Dashdest_file = directory + Dashname
Dashsrc_file = '/home/pi/Desktop/CarPiTouch/Frontoutput.avi'
Revdest_file = directory + Revname
Revsrc_file = '/home/pi/Desktop/CarPiTouch/output.avi'


	
def copyoutput():
	shutil.copy2(Dashsrc_file, Dashdest_file)
	print(str(datetime.datetime.now()) + 'Moving Output files')
	shutil.copy2(Revsrc_file, Revdest_file)


if __name__ == '__main__':
	copyoutput()


	
	
