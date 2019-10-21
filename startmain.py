#Import Libraries
#import RPi.GPIO as GPIO
import time
import os
import datetime
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
from multiprocessing import Pool
#Dashcam = "/home/pi/Desktop/Cam/Dashcam.py"
#Reversecam = "/home/pi/Desktop/Cam/ReverseCam.py"
Dashcam = "Dashcam.py"
Reversecam = "ReverseCam.py"
GUI = "GUI.py"
DebugInfo = ' [Info] '
DebugWarn = ' [Warning] '
DebugErr = ' [Error] '

loaded = False
gpsdd = False




def loadedcheck()
	if gpsdd == True and 
def run_process(process):                                                             
    os.system('python {}'.format(process))


if __name__ == '__main__':
	print(str(datetime.datetime.now()) + ' Running NavIt ') #Debug 1
	#os.system('navit')

	gpsdstatus = os.system('systemctl is-active --quiet gpsd') # will return 0 for active else inactive
	if gpsdstatus == 0:
		print(str(datetime.datetime.now()) + DebugInfo + 'GPSD active')
		gpsdd = True
	else:
		print(str(datetime.datetime.now()) + DebugWarn + 'GPSD not Active, Service not started or Error thrown')
		print(str(datetime.datetime.now()) + DebugInfo + 'Attempting Restart of GPSD')
		os.system('sudo killall gpsd')
		print(str(datetime.datetime.now()) + DebugInfo + 'Killed all gpsd instances')
		os.system('sudo rm /var/run/gpsd.sock')
		print(str(datetime.datetime.now()) + DebugInfo + 'Removing any sockets gpsd may have left')
		os.system('sudo gpsd /dev/serial0 -F /var/run/gpsd.sock')
		print(str(datetime.datetime.now()) + DebugInfo + 'Restarting GPSD')
		gpsdstatus = os.system('systemctl is-active --quiet gpsd') # will return 0 for active else inactive
		if gpsdstatus == 0:
			print(str(datetime.datetime.now()) + DebugInfo + 'GPSD now active')
			gpsdd = True
		else:
			print(str(datetime.datetime.now()) + DebugErr + 'GPSD Unable to be started')
		
		
	print(str(datetime.datetime.now()) + DebugInfo +'Starting ReverseCam script')
	print(str(datetime.datetime.now()) + DebugInfo + 'Starting Dashcam script')
	processes = (Dashcam, Reversecam, GUI)
	pool = Pool(processes=3)                                                        
	pool.map(run_process, processes)  
	
	


	
	
