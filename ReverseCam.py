#Import Libraries
import cv2
import RPi.GPIO as GPIO
import time
import numpy as np
import datetime
import os
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
from startmain import DebugInfo
from startmain import DebugWarn
from startmain import DebugErr
print(str(datetime.datetime.now()) + DebugInfo + 'Successfully Imported Reversecam libaries') #Debug 1

GPIO.setwarnings(False)
gpiopin=36
gpiocheck1=35
cam = ""
videoOut = ""

def SETGPIO():
	#Set up GPIO PIN 
	GPIO.setmode(GPIO.BOARD)
	#Set Pin 36 as input for camera switch
	GPIO.setup(gpiopin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	print(str(datetime.datetime.now()) + DebugInfo + 'GPIO pin 36 configured as rvc') #Debug 1
	GPIO.setup(gpiocheck1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	print(str(datetime.datetime.now()) + DebugInfo + 'GPIO pin 35 configured as rvchk') 

def InitaliseCam():
	global cam
	global videoOut
	print(str(datetime.datetime.now()) + DebugInfo + 'Initalising  Reversecam CV2 ') #Debug 1
	#Set up Video Input and Codec
	camera_port = 2
	cam = cv2.VideoCapture(camera_port)
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	videoOut = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))
	print(str(datetime.datetime.now()) + DebugInfo + 'Initalised Reversecam CV2 ') #Debug 1

def Destroy():
	cv2.destroyAllWindows()

def EndProg():
	print(str(datetime.datetime.now()) + DebugInfo + 'Reversecam Stopped') #Debug 3
	cam.release()
	videoOut.release()
	cv2.destroyAllWindows()
	

	
if __name__ == "__main__":
	# stuff only to run when not called via 'import' here
	InitaliseCam()
	SETGPIO()
	while True:
		camoff=False
		ret,frame = cam.read()
		if ret == True: 
			# Write the frame into the file 'output.avi'
			videoOut.write(frame)
		if (GPIO.input(gpiopin) ==1): ##This will happen if var1 == true
			print(str(datetime.datetime.now()) + DebugInfo + 'Detected Input Enabling Reversing Camera')
			while (GPIO.input(gpiopin) ==1):
				ret,frame = cam.read()
				if ret == True: 
					videoOut.write(frame)
					#Create Fullscreen Preview of Camera 
					cv2.namedWindow('webcam', cv2.WND_PROP_FULLSCREEN)
					cv2.setWindowProperty('webcam',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
					cv2.imshow('webcam', frame)
					#if Q is pressed break function
					camoff = True
					if cv2.waitKey(1)&0xFF == ord('q'):
						Destroy()
						break
				else:
					print(str(datetime.datetime.now()) + DebugErr +"Unable to read Reversing Camera")
					break
			if (GPIO.input(gpiopin)==0) and camoff==True:
				camoff=False
				Destroy()
		if (GPIO.input(gpiocheck1) ==1):
			break
	EndProg()

