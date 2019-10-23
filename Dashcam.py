#Import Libraries
import cv2
import time
import numpy as np
import datetime
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
x = "Y"
fileout = str(datetime.datetime.now()) + " Frontoutput.avi"
from startmain import DebugInfo
from startmain import DebugWarn
from startmain import DebugErr

print(str(datetime.datetime.now()) + DebugInfo + 'Successfully Imported Dashcam libaries') #Debug 1

def InitaliseCV():
	global cam
	global videoOut
	print(str(datetime.datetime.now()) + DebugInfo + 'Initalising Dashcam CV2 ') #Debug 1
	#Set up Video Input and Codec
	camera_port = 0
	cam = cv2.VideoCapture(camera_port)
	time.sleep(2) #Int Cam 
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	videoOut = cv2.VideoWriter(fileout, fourcc, 10.0, (800, 480))
	print(str(datetime.datetime.now()) + DebugInfo + 'Initalised Dashcam CV2 ') #Debug 1
def CamRecord():
	if x == "Y":
		while True:
			ret,frame = cam.read()
			if ret == True: 
				# Write the frame into the file 'Frontoutput.avi'
				videoOut.write(frame)
			else:
				print(str(datetime.datetime.now()) + DebugErr + "Unable to read Dashcam Camera")
				break
def display():
	ret,frame = cam.read()
	if ret == True: 
		videoOut.write(frame)
		#Create Fullscreen Preview of Camera 
		cv2.namedWindow('Dashcam', cv2.WND_PROP_FULLSCREEN)
		cv2.setWindowProperty('Dashcam',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
		cv2.imshow('Dashcam', frame)
		#if Q is pressed break function
		if cv2.waitKey(1)&0xFF == ord('q'):
			cv2.destroyAllWindows()
			return
	else:
		print(str(datetime.datetime.now()) + DebugErr +"Unable to read Dash Camera")
		return
def Destroy():
	cv2.destroyAllWindows()

def EndProg():
	print(str(datetime.datetime.now()) + DebugInfo + 'Dashcam Stopped') #Debug 1
	cam.release()
	videoOut.release()
	cv2.destroyAllWindows()	
		
if __name__ == '__main__':
	InitaliseCV()
	CamRecord()
	EndProg()