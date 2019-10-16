#Import Libraries
import cv2
import time
import numpy as np
import datetime
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
x = "Y"

print(str(datetime.datetime.now()) + ' Successfully Imported Dashcam libaries') #Debug 1

print(str(datetime.datetime.now()) + ' Initalising Dashcam CV2 ') #Debug 1
#Set up Video Input and Codec
camera_port = 2
cam = cv2.VideoCapture(camera_port)
time.sleep(2) #Int Cam 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
videoOut = cv2.VideoWriter("Frontoutput.avi", fourcc, 10.0, (640, 480))
print(str(datetime.datetime.now()) + ' Initalised Dashcam CV2 ') #Debug 1


if x == "Y":
	while True:
		ret,frame = cam.read()
		if ret == True: 
			# Write the frame into the file 'Frontoutput.avi'
			videoOut.write(frame)
		else:
			print(str(datetime.datetime.now()) + " Unable to read Camera")
			break

print(str(datetime.datetime.now()) + ' Dashcam Stopped') #Debug 1
cam.release()
videoOut.release()
cv2.destroyAllWindows()
