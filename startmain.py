#Import Libraries
#import RPi.GPIO as GPIO
import time
import os
import datetime
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
from multiprocessing import Pool
import subprocess
#Dashcam = "/home/pi/Desktop/Cam/Dashcam.py"
#Reversecam = "/home/pi/Desktop/Cam/ReverseCam.py"

#Dashcam = "Dashcam.py"
Reversecam = "ReverseCam.py"
GUI = "GUI.py"

DebugInfo = ' [Info] '
DebugWarn = ' [Warning] '
DebugErr = ' [Error] '


def run_process(process):                                                             
    os.system('python {}'.format(process))
	
def run_Navit():
	Navitstatus = os.system('systemctl is-active --quiet navit') # will return 0 for active else inactive
	if Navitstatus == 0:
		print(str(datetime.datetime.now()) + DebugInfo + 'Navit Active')
		
	else:
		print(str(datetime.datetime.now()) + DebugWarn + 'Navit not Active, Service not started or Error thrown')
		print(str(datetime.datetime.now()) + DebugInfo + ' Restarting NavIt ') #Debug 1
		subprocess.Popen(['navit'])
		Navitstatusstatus = os.system('systemctl is-active --quiet navit') # will return 0 for active else inactive
		if Navitstatus == 0:
			print(str(datetime.datetime.now()) + DebugInfo + 'Navit now running')
			
		else:
			print(str(datetime.datetime.now()) + DebugErr + 'Navit Unable to be started')
	
	
	
def gpsd():
	gpsdstatus = os.system('systemctl is-active --quiet gpsd') # will return 0 for active else inactive
	if gpsdstatus == 0:
		print(str(datetime.datetime.now()) + DebugInfo + 'GPSD active')
		
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
			
		else:
			print(str(datetime.datetime.now()) + DebugErr + 'GPSD Unable to be started')

if __name__ == '__main__':
	gpsd()
	run_Navit()
	
	print(str(datetime.datetime.now()) + DebugInfo +'Starting ReverseCam script')
	print(str(datetime.datetime.now()) + DebugInfo + 'Starting Dashcam script')
	print(str(datetime.datetime.now()) + DebugInfo + 'Starting GUI')
	processes = (Reversecam, GUI)
	pool = Pool(processes=2)                                                        
	pool.map(run_process, processes)  
	
	


	
	
