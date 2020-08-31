#Import Libraries
import cv2
import time
import numpy as np
import datetime
import RPi.GPIO as GPIO
import picamera
import os
import psutil

datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
GPIO.setwarnings(False)
from startmain import DebugInfo
from startmain import DebugWarn
from startmain import DebugErr

MAX_FILES = 999
DURATION = 1
SPACE_LIMIT = 80

file_root = "/media/pi/6EAA-CEC11/footage/Dash"

if(psutil.disk_usage(".").percent > SPACE_LIMIT):
	print(str(datetime.datetime.now()) + DebugErr + "WARNING: Low space!")
	exit()
print(str(datetime.datetime.now()) + DebugInfo + 'Successfully Imported Dashcam libaries') #Debug 1

gpiocheck=33
def Initalise():
	if not os.path.exists(file_root):
		print(str(datetime.datetime.now()) + DebugWarn +'Creating Dash Footage Dir')
		os.makedirs(file_root)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(gpiocheck, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	print(str(datetime.datetime.now()) + DebugInfo + 'GPIO pin 33 configured as dhchk') 
	print(str(datetime.datetime.now()) + DebugInfo + 'Initalising Dashcam') #Debug 1
	
def CamRecord():
	with picamera.PiCamera() as camera:
		camera.resolution = (1920,1080)
		camera.framerate = 30

		print('Searching files...')
		for i in range(1, MAX_FILES):
			file_number = i
			file_name = file_root + "video" + str(i).zfill(3) + ".h264"
			exists = os.path.isfile(file_name)
			if not exists:
				print "Search complete"
				break

		for file_name in camera.record_sequence(file_root + "video%03d.h264" % i for i in range(file_number, MAX_FILES)):
			print('Recording to %s' % file_name)
			camera.wait_recording(DURATION*60)
			if(psutil.disk_usage(".").percent > SPACE_LIMIT):
				print(str(datetime.datetime.now()) + DebugWarn + "WARNING: Low space!")
				break;
				
			
			if (GPIO.input(gpiocheck) ==1):
				break
			
if __name__ == '__main__':
	Initalise()
	CamRecord()
	
