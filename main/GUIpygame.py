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
paused = True


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
		
	def PlayPause(x,y,w,h):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if paused:
			imagechange = playpic
		else: 
			imagechange = pausepic
		if x+w > mouse[0] > x and y+h > mouse[1] > y:
			pygame.draw.rect(Display, BACKGROUND,(x,y,w,h))
			if click[0] == 1:
				if paused:
					paused = False
				else:
					paused = True
		else:
			pygame.draw.rect(Display, BACKGROUND,(x,y,w,h))
		Display.blit(imagechange, (x,y))
	def SkipForward(x,y,w,h):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if x+w > mouse[0] > x and y+h > mouse[1] > y:
			pygame.draw.rect(Display, BACKGROUND,(x,y,w,h))
			if click[0] == 1:
				skipforwards()
		else:
			pygame.draw.rect(Display, BACKGROUND,(x,y,w,h))
		Display.blit(skipff, (x,y))
	def SkipBack(x,y,w,h):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if x+w > mouse[0] > x and y+h > mouse[1] > y:
			pygame.draw.rect(Display, BACKGROUND,(x,y,w,h))
			if click[0] == 1:
				skipbackwards()
		else:
			pygame.draw.rect(Display, BACKGROUND,(x,y,w,h))
		Display.blit(skiprr, (x,y))
	def bottomuibar():
		pygame.draw.rect(Display, black, (0,500,800,100))
		#play pause back forward
		#if volume is certain level do speaker
	

def skipforwards():		
	thing = True
def skipbackwards():
	thing = True

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
			x = True
			return x
		
	else:
		pygame.draw.rect(Display, ic,(x,y,w,h))
		x = False
		
	
	smallText = pygame.font.Font("freesansbold.ttf",20)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	Display.blit(textSurf, textRect)
	return x
	#msg Button text
	#x coor
	#y coor
	#w width
	#h height
	#ic Standard colour
	#ac On Hover colour


class Windows:
	def mainScreen():
		while True:
			#print(str(datetime.datetime.now()) + DebugInfo + 'Main Menu')
			for event in pygame.event.get():
				#print(event)
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				
			Display.fill(darkblue)
			
			Icons.bottomuibar()
			pygame.display.flip()
			clock.tick(15)



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
	
	Fullvol = pygame.image.load(imgdir +'\speaker-xxl.png')
	halfvol = pygame.image.load(imgdir +'\MiniSpeaker.png')
	lowvol = pygame.image.load(imgdir +'\MiniSpeakerno.png')
	mutevol = pygame.image.load(imgdir +'\speakermute.png')

	skipff = pygame.image.load(imgdir +'\Doublearrow.png')
	skiprr = pygame.image.load(imgdir +'\Doublearrowback.png')
	pausepic = pygame.image.load(imgdir +'\pause.png')
	playpic = pygame.image.load(imgdir +'\Play.png')
	print(str(datetime.datetime.now()) + DebugInfo + 'Images Loaded')
	
	Windows.mainScreen()
	pygame.quit()
	quit()

def unessiary_shite():
		#and action != None
		#largeText = pygame.font.Font('freesansbold.ttf',115)
		#TextSurf, TextRect = text_objects("A bit Racey", largeText)
		#TextRect.center = ((display_width/2),(display_height/2))
		#Display.blit(TextSurf, TextRect)
		print('end')