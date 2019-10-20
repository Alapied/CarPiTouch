#Import Libraries
import cv2
#import RPi.GPIO as GPIO
import time
import numpy as np
import os
import datetime
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
from startmain import DebugInfo
from startmain import DebugWarn
from startmain import DebugErr
print(str(datetime.datetime.now()) + DebugInfo + 'Successfully Imported Reversecam libaries') #Debug 1

print(str(datetime.datetime.now()) + DebugInfo + 'Initalising  Reversecam CV2 ') #Debug 1
#Set up Video Input and Codec
camera_port = 0
cam = cv2.VideoCapture(camera_port + cv2.CAP_DSHOW)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
videoOut = cv2.VideoWriter("output.avi", fourcc, 10.0, (640, 480))
print(str(datetime.datetime.now()) + DebugInfo + 'Initalised Reversecam CV2 ') #Debug 1


def SETGPIO():
		#Set up GPIO PIN 
		#GPIO.setmode(GPIO.BOARD)
		#Set Pin 11 as input for reversing camera signal switch
		#GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		x = "Y"
		print(str(datetime.datetime.now()) + DebugInfo + 'GPIO pins configured') #Debug 1
		
def EndProg():
	print(str(datetime.datetime.now()) + DebugInfo + 'Reversecam Stopped') #Debug 3
	cam.release()
	videoOut.release()
	Destroy()
	#GPIO.cleanup()

def Destroy():
	cv2.destroyAllWindows()

def Opencam():
	ret,frame = cam.read()
	if ret == True: 
		#Create Fullscreen Preview of Camera 
		cv2.namedWindow('webcam', cv2.WND_PROP_FULLSCREEN)
		cv2.setWindowProperty('webcam',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
		cv2.imshow('webcam', frame)
		#if Q is pressed break function
		if cv2.waitKey(1)&0xFF == ord('q'):
			cv2.destroyAllWindows()
			return
	else:
		print(str(datetime.datetime.now()) + DebugErr +"Unable to read Reversing Camera")
		return
				
if __name__ == "__main__":
	# stuff only to run when not called via 'import' here
	
	SETGPIO()
	while True:
		#var1=GPIO.input(11)
		var1 = True
		
		ret,frame = cam.read()
		if ret == True: 
			# Write the frame into the file 'output.avi'
			videoOut.write(frame)
		if var1: ##This will happen if var1 == true
			print(str(datetime.datetime.now()) + DebugInfo + 'Detected Input from Pin 11 Enabling Reversing Camera')
			while var1:
				Opencam()
			cv2.destroyAllWindows()
	EndProg()