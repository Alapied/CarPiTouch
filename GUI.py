#from tkinter import mainloop
from ast import If
from msilib.schema import Icon
from tkinter import W
import pygame
import os
#from ReverseCam import Destroy
#from ReverseCam import display
#from ReverseCam import camInt
#from ReverseCam import InitaliseCam
import time
import datetime
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)

i=1
imgdir = "resources\icons"
DebugInfo = ' [Info] '
DebugWarn = ' [Warning] '
DebugErr = ' [Error] '
globalMenustate = 0
volume = 1.0

class Icons:
	def GPSIcon(x,y):
		Display.blit(GPSImg, (x,y))
		pygame.display.flip()
		
	def MapsIcon(x,y,w,h):
		#Display.blit(MapsImg, (x,y))
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if x+w > mouse[0] > x and y+h > mouse[1] > y:
			pygame.draw.rect(Display, BACKGROUND,(x,y,w,h))
			if click[0] == 1:
				print('f')
		
		else:
			pygame.draw.rect(Display, BACKGROUND,(x,y,w,h))
		Display.blit(MapsImg, (x,y))
		
		
	def CamIcon(x,y,w,h):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if x+w > mouse[0] > x and y+h > mouse[1] > y:
			pygame.draw.rect(Display,BACKGROUND,(x,y,w,h))
			if click[0] == 1:
				print("Cam")
		else:
			pygame.draw.rect(Display, BACKGROUND,(x,y,w,h))
		Display.blit(CamRecImg, (x,y))
		
		
	def SettingsIcon(x,y):
		Display.blit(settingImg, (x,y))
		pygame.display.flip()

	def bottomuibar():
		pygame.draw.rect(Display, black, (0,500,800,100))
		#play pause back forward
		#if volume is certain level do speaker
	def pythonIcon(x,y):
		global i
		pythonImg.set_alpha(i)
		Display.blit(pythonImg, (x,y))
		pygame.time.delay(20)
		i+=3
		if i==255:
			i=1
			time.sleep(2)

		

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()
 
def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	Display.blit(TextSurf, TextRect)
 
	pygame.display.update()
 
	time.sleep(2)

def button(msg,x,y,w,h,ic,ac):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(Display, ac,(x,y,w,h))
		if click[0] == 1:
			print('f')
		
	else:
		pygame.draw.rect(Display, ic,(x,y,w,h))
	
	smallText = pygame.font.Font("freesansbold.ttf",20)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	Display.blit(textSurf, textRect)
	#msg Button text
	#x coor
	#y coor
	#w width
	#h height
	#ic Standard colour
	#ac On Hover colour

def MapsButton(msg,x,y,w,h,ic,ac):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(Display, ac,(x,y,w,h))
		
		if click[0] == 1:
			Windows.TestScreen()
			os.system('wmctrl -a navit')
	else:
		pygame.draw.rect(Display, ic,(x,y,w,h))
	
	smallText = pygame.font.Font("freesansbold.ttf",20)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	
	Display.blit(textSurf, textRect)
	#msg Button text
	#x coor
	#y coor
	#w width
	#h height
	#ic Standard colour
	#ac On Hover colour

class Windows:
	def Load():
		#Only here to allow the other scripts time to finish the start phase and look a bit cool
		print(str(datetime.datetime.now()) + DebugInfo + 'Loading Main Menu')
		t_end = time.time() + 6
		while time.time() < t_end:		
			Display.fill(black)
			Icons.pythonIcon (display_width/2, display_height/2)
			pygame.display.flip()
		global globalMenustate 
		globalMenustate = 1

	def mainScreen():
		#print(str(datetime.datetime.now()) + DebugInfo + 'Main Menu')
		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
		Display.fill(darkblue)
			
			
		Icons.MapsIcon(x/6,y/8,140,140)
		Icons.GPSIcon (x/1.3, y/8)
		#Icons.CamIcon (x*1.8,y/8.9,140,140)
		Icons.bottomuibar()
		pygame.display.flip()
		clock.tick(15)

	def TestScreen():
		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
		Display.fill(blue)
		Icons.MapsIcon(x/6,y/8,140,140)
		Icons.GPSIcon (x/1.3, y/8)
			
		pygame.display.update()
		clock.tick(15)

def menuselector(menuState):
	#print(menuState)
	#print(globalMenustate)
	if menuState == 0:
		Windows.Load()
	elif menuState == 1:
		Windows.mainScreen()
	elif menuState == 2:
		Windows.TestScreen()
	else:
		print(menuState,str(datetime.datetime.now()) + DebugErr + 'Incorrect Menu selected')

def mainmenuloop():
	while True:
		menuselector(globalMenustate)


if __name__ == '__main__':
	pygame.init()
	print(str(datetime.datetime.now()) + DebugInfo + 'pygame Initialised')
	display_width = 800
	display_height = 600
	x =  (display_width * 0.45)
	y = (display_height * 0.8)
	centreScreen = (display_width/2, display_height/2)
	Display = pygame.display.set_mode((display_width,display_height))
	pygame.display.set_caption('testGUI')
	black = (0,0,0)
	white = (255,255,255)
	blue = (0, 66, 89)
	darkblue = (0, 0, 66)
	red = (255,0,0)
	green = (0,200,0)
	BACKGROUND = darkblue
	clock = pygame.time.Clock()
	crashed = False
	print(str(datetime.datetime.now()) + DebugInfo + 'pygame accesories loaded')

	phoneImg = pygame.image.load(imgdir +'\Phone.png')
	bluetoothImg = pygame.image.load(imgdir +'\Bluetooth.png')
	homeImg = pygame.image.load(imgdir +'\Home.png')
	MapsImg = pygame.image.load(imgdir +'\Maps.png')
	settingImg = pygame.image.load(imgdir +'\Settings.png')
	GPSImg = pygame.image.load(imgdir +'\Satellite.png')
	CamRecImg = pygame.image.load(imgdir +'\Recorder.png')
	
	Fullvol = pygame.image.load(imgdir +'\speaker-xxl.png')
	halfvol = pygame.image.load(imgdir +'\MiniSpeaker.png')
	lowvol = pygame.image.load(imgdir +'\MiniSpeakerno.png')
	mutevol = pygame.image.load(imgdir +'\speakermute.png')

	skipff = pygame.image.load(imgdir +'\Doublearrow.png')
	skiprr = pygame.image.load(imgdir +'\Doublearrowback.png')
	pausepic = pygame.image.load(imgdir +'\pause.png')
	playpic = pygame.image.load(imgdir +'\Play.png')

	pythonImg = pygame.image.load(imgdir +'\Python.png')
	pythonImg = pythonImg.convert()
	print(str(datetime.datetime.now()) + DebugInfo + 'Images Loaded')
	
	mainmenuloop()
	pygame.quit()
	quit()

def unessiary_shite():
		#and action != None
		#largeText = pygame.font.Font('freesansbold.ttf',115)
		#TextSurf, TextRect = text_objects("A bit Racey", largeText)
		#TextRect.center = ((display_width/2),(display_height/2))
		#Display.blit(TextSurf, TextRect)
		print('end')