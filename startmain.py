#! /usr/bin/python

#Import Libraries
import RPi.GPIO as GPIO
import time
import os
import datetime
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
from multiprocessing import Pool
import subprocess

#Dashcam = "/home/pi/Desktop/CarPiTouch/Dashcam.py"
Reversecam = "/home/pi/Desktop/CarPiTouch/ReverseCam.py"
Shutdown = "/home/pi/Desktop/CarPiTouch/shutdown.py"

#Dashcam = "Dashcam.py"
#Reversecam = "ReverseCam.py"
#Shutdown = "shutdown.py"
directory = '/media/pi/6EAA-CEC1/footage'
DebugInfo = ' [Info] '
DebugWarn = ' [Warning] '
DebugErr = ' [Error] '


def run_process(process):                                                             
    os.system('python {}'.format(process))
	
def run_Navit():
	print(str(datetime.datetime.now()) + DebugInfo + 'Marker: Navit Started')
	Navitstatus = os.system('systemctl is-active --quiet navit') # will return 0 for active else inactive
	if Navitstatus == 0:
		print(str(datetime.datetime.now()) + DebugInfo + 'Navit Active')
		
	else:
		print(str(datetime.datetime.now()) + DebugWarn + 'Navit process not running, Service not started or error has been thrown')
		print(str(datetime.datetime.now()) + DebugInfo + ' Restarting NavIt ') #Debug 1
		subprocess.Popen(['navit'])
		time.sleep(1)
		Navitstatusstatus = os.system('systemctl is-active --quiet navit') # will return 0 for active else inactive
		if Navitstatus == 0:
			print(str(datetime.datetime.now()) + DebugInfo + 'Navit now running')
			#informs console that Navit is running
		else:
			print(str(datetime.datetime.now()) + DebugErr + 'Navit Unable to be started')
	
	
	
def gpsd():
	print(str(datetime.datetime.now()) + DebugInfo + 'Marker: GPSD Started')
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
			

def setgpio():
	print(str(datetime.datetime.now()) + DebugInfo + 'Marker: GPIO Started')
	GPIO.setwarnings(False)
	print(str(datetime.datetime.now()) + DebugInfo + 'GPIO Warnings set to false')
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	print(str(datetime.datetime.now()) + DebugInfo + 'GPIO 37 prepped')
	GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	print(str(datetime.datetime.now()) + DebugInfo + 'GPIO 36 prepped')
	GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(11, GPIO.OUT)
	GPIO.output(11, GPIO.LOW)
	print(str(datetime.datetime.now()) + DebugInfo + 'GPIO Rev Pins 11 and 35 prepped')
	GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(13, GPIO.LOW)
	print(str(datetime.datetime.now()) + DebugInfo + 'GPIO Dash Pins 13 and 33 prepped')
	
if __name__ == '__main__':
	print(str(datetime.datetime.now()) + DebugInfo +'Beginning Startup process')
	if not os.path.exists(directory):
		print(str(datetime.datetime.now()) + DebugWarn +'Creating Footage Dir')
		os.makedirs(directory)
	setgpio()
	gpsd()
	run_Navit()
			
	print(str(datetime.datetime.now()) + DebugInfo +'Starting ReverseCam script')
	processes = (Reversecam, Shutdown)
	pool = Pool(processes=2)
	pool.map(run_process, processes)  
	print("after")
