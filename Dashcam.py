#Import Libraries
import cv2
import time
import numpy as np
import datetime
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
x = "Y"

from startmain import DebugInfo
from startmain import DebugWarn
from startmain import DebugErr

print(str(datetime.datetime.now()) + DebugInfo + 'Successfully Imported Dashcam libaries') #Debug 1

cam = ""
videoOut = ""
def InitaliseCV():
	global cam
	global videoOut
	print(str(datetime.datetime.now()) + DebugInfo + 'Initalising Dashcam CV2 ') #Debug 1
	#Set up Video Input and Codec
	camera_port = 0
	cam = cv2.VideoCapture(camera_port)
	time.sleep(2) #Int Cam 
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	videoOut = cv2.VideoWriter("Frontoutput.avi", fourcc, 10.0, (800, 480))
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
				time.sleep(2)
				
def EndProg1():
	print(str(datetime.datetime.now()) + DebugInfo + 'Dashcam Stopped') #Debug 1
	cam.release()
	videoOut.release()
	cv2.destroyAllWindows()	
		
if __name__ == '__main__':
	InitaliseCV()
	CamRecord()
	
