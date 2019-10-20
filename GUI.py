import pygame
imgdir = "resources\icons"
from ReverseCam import Opencam
from ReverseCam import Destroy
pygame.init()
import time

display_width = 800
display_height = 600
x =  (display_width * 0.45)
y = (display_height * 0.8)
centreScreen = (display_width/2, display_height/2)
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('testGUI')

black = (0,0,0)
white = (255,255,255)
blue = (0, 66, 89)
darkblue = (0, 0, 66)
red = (255,0,0)
green = (0,200,0)

clock = pygame.time.Clock()
crashed = False

phoneImg = pygame.image.load(imgdir +'\Phone.png')
bluetoothImg = pygame.image.load(imgdir +'\Bluetooth.png')
homeImg = pygame.image.load(imgdir +'\Home.png')
MapsImg = pygame.image.load(imgdir +'\Maps.png')
settingImg = pygame.image.load(imgdir +'\Settings.png')
GPSImg = pygame.image.load(imgdir +'\Satellite.png')
CamRecImg = pygame.image.load(imgdir +'\Recorder.png')


class Icons:
	def GPSIcon(x,y):
		gameDisplay.blit(GPSImg, (x,y))
		
	def MapsIcon(x,y,w,h):
		#gameDisplay.blit(MapsImg, (x,y))
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if x+w > mouse[0] > x and y+h > mouse[1] > y:
			pygame.draw.rect(gameDisplay, blue,(x,y,w,h))
			if click[0] == 1:
				print('f')
		
		else:
			pygame.draw.rect(gameDisplay, blue,(x,y,w,h))
		gameDisplay.blit(MapsImg, (x,y))
		
	def CamIcon(x,y,w,h):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if x+w > mouse[0] > x and y+h > mouse[1] > y:
			pygame.draw.rect(gameDisplay, blue,(x,y,w,h))
			if click[0] == 1:
				t_end = time.time() + 15
				while time.time() < t_end:
					Opencam()
				Destroy()
		else:
			pygame.draw.rect(gameDisplay, blue,(x,y,w,h))
		gameDisplay.blit(CamRecImg, (x,y))
		
	def SettingsIcon(x,y):
		gameDisplay.blit(settingImg, (x,y))
		
		

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()
 
def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf, TextRect)
 
	pygame.display.update()
 
	time.sleep(2)

def button(msg,x,y,w,h,ic,ac):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
		if click[0] == 1:
			print('f')
		
	else:
		pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
	
	smallText = pygame.font.Font("freesansbold.ttf",20)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	gameDisplay.blit(textSurf, textRect)
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
		pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
		
		if click[0] == 1:
			Windows.TestScreen()
	else:
		pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
	
	smallText = pygame.font.Font("freesansbold.ttf",20)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	
	gameDisplay.blit(textSurf, textRect)
	#msg Button text
	#x coor
	#y coor
	#w width
	#h height
	#ic Standard colour
	#ac On Hover colour

class Windows:
	def Load():
		load = True
		load = False
	def mainScreen():
		main = True
		while main:
			for event in pygame.event.get():
				#print(event)
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			
			gameDisplay.fill(darkblue)
			
			
			Icons.MapsIcon(x/6,y/8,140,140)
			Icons.GPSIcon (x/1.3, y/8)
			Icons.CamIcon (x*1.7,y/8,140,140)
			MapsButton("GO!",150,450,100,50,green,blue)
			button("Quit",550,450,100,50,red,black)
			
			
			pygame.display.update()
			clock.tick(15)

	def TestScreen():
		test = True
		while test:
			for event in pygame.event.get():
				#print(event)
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			
			gameDisplay.fill(blue)
			Icons.MapsIcon(x/6,y/8,140,140)
			Icons.GPSIcon (x/1.3, y/8)
			
			pygame.display.update()
			clock.tick(15)
Windows.Load()		
Windows.mainScreen()
pygame.quit()
quit()

def unessiary_shite():
		#and action != None
		#largeText = pygame.font.Font('freesansbold.ttf',115)
		#TextSurf, TextRect = text_objects("A bit Racey", largeText)
		#TextRect.center = ((display_width/2),(display_height/2))
		#gameDisplay.blit(TextSurf, TextRect)
		print('end')