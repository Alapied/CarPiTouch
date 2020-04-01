#Import Libraries
import cv2
import time
import numpy as np
import datetime
import RPi.GPIO as GPIO
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
GPIO.setwarnings(False)

from startmain import DebugInfo
from startmain import DebugWarn
from startmain import DebugErr

print(str(datetime.datetime.now()) + DebugInfo + 'Successfully Imported Dashcam libaries') #Debug 1

camd = ""
videodOut = ""
gpiocheck=33
def InitaliseCV():
	global camd
	global videodOut
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(gpiocheck, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	print(str(datetime.datetime.now()) + DebugInfo + 'GPIO pin 33 configured as dhchk') 
	print(str(datetime.datetime.now()) + DebugInfo + 'Initalising Dashcam CV2 ') #Debug 1
	#Set up Video Input and Codec
	camera_port = 0
	camd = cv2.VideoCapture(camera_port)
	time.sleep(2) #Int Cam 
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	camd.set(cv2.CAP_PROP_FOURCC, fourcc)
	videodOut = cv2.VideoWriter("Frontoutput.avi", fourcc, 20.0, (640, 480))
	print(str(datetime.datetime.now()) + DebugInfo + 'Initalised Dashcam CV2 ') #Debug 1
def CamRecord():
	while True:
		ret,frame = camd.read()
		if ret == True: 
			# Write the frame into the file 'Frontoutput.avi'
			videodOut.write(frame)
		else:
			print(str(datetime.datetime.now()) + DebugErr + "Unable to read Dashcam Camera")
		
		if (GPIO.input(gpiocheck) ==1):
			break
	EndProg1()
	
def EndProg1():
	print(str(datetime.datetime.now()) + DebugInfo + 'Dashcam Stopped') #Debug 1
	cam.release()
	videodOut.release()
	cv2.destroyAllWindows()	
		
if __name__ == '__main__':
	InitaliseCV()
	CamRecord()
	
