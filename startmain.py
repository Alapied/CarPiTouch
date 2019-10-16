#Import Libraries
#import RPi.GPIO as GPIO
import time
import os
import datetime
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
from multiprocessing import Pool
Dashcam = "/home/pi/Desktop/Cam/Dashcam.py"
Reversecam = "/home/pi/Desktop/Cam/ReverseCam.py"

def run_process(process):                                                             
    os.system('python {}'.format(process))

if __name__ == '__main__':
	print(str(datetime.datetime.now()) + ' Running NavIt ') #Debug 1
	#os.system('navit')

	print(str(datetime.datetime.now()) + ' Successfully Imported libaries') #Debug 1
	print(str(datetime.datetime.now()) + ' Booting ReverseCam')
	print(str(datetime.datetime.now()) + ' Booting Dashcam')
	processes = (Dashcam, Reversecam)
	pool = Pool(processes=2)                                                        
	pool.map(run_process, processes)  
	


	
	
