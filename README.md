# CarPiTouch
If you wanted to have one of those fancy touchscreens in your car but instead of paying money for some companies piece of shit software you could use an open-source solution? Well i present my project as a solution to that problem. 

## The Key Idea
This is project to use a raspberry pi as a head unit within your car, with an intuitive GUI with Navit based maps, and Reversing/Dash camera functionality, also using mikebrady's shairport-sync to allow audio to be played as well. The goal is to eventually get to a state where this is working as a full blown hardware device, so that instructions can be easily followed

## What i did (i think)
These are the steps i took on a Raspberry Pi 4, there are things that changed during development so have a watchful eye
### Prep SD card Image and Pi
*Flash Rasbian Buster LITE to an SD card (8GB or greater) -- Current version at time of writing
*Boot the raspi for the first time, u know the usual tinkering
*Connect the Pi to the internet through ethernet or via the raspi config
```
$ sudo raspi-config
```
*Update the pi 
```
$ sudo apt-get update
$ sudo apt-get upgrade
```
*Install The Desktop Enviroment
```
$ sudo apt-get install raspberrypi-ui-mods
```
Once installed enter the raspi config and set the pi to boot to desktop
### Install Python and its dependancies
* Install Python 3.6 and Pip - Works for some reason
```
$ sudo apt-get install python3.6
$ sudo apt-get install python3-pip
```
* Install OpenCV, NumPy and RPi.GPIO
```
$ sudo apt-get install python3-opencv
$ sudo pip3 install RPi.GPIO
$ sudo apt-get install libqt4-test
```
Note: I went through so many missing dependancies this list here will grow i just didnt document
### The navigation and audio controls
* Install Navit and espeak
```
$ sudo apt-get install navit espeak
```
* Install Kodi for non rpi4 users (optional)
```
$ sudo apt-get install kodi
```

### Shareport Sync

## The issues
It was a really pain in the ass to install all the dependancies for Opencv Python (cv2) and try and get the multiple cameras working simutaniously, a bunch of firmware and bandwidth issues are present in the basic working product which refused to work.
I haven't documented things well, this could use someone who knows what they're doing.
