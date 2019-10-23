# CarPiTouch

A project to use a raspberry pi as a head unit within a car, with an intuitive GUI with maps, and Reversing/Dash Camera functionality

It does however require a lot of Libaries to install

# Installation instructions

//TODO
Update 
Sudo apt-get update
Sudo apt-get upgrade

Install Raspian GUI
Sudo apt-get install raspberrypi-ui-mods
Once installed enter raspiconfig and set boot options: splash no, boot to desktop yes

Change audio out and expand filesystem in raspi config 
Sudo raspi-config

Install necessary python software
Sudo apt-get install python3.6
Sudo apt-get install python3-pip
Sudo apt-get install python3-opencv  //installs numpy as well, errors may occur so install dependacys for cv2
sudo apt install libqt4-test
Pip3 install RPi.GPIO 

Install Navit
Sudo apt-get navit espeak
