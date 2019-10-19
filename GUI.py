import pygame
imgdir = "resources\icons"

pygame.init()


display_width = 800
display_height = 600

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



def GPSIcon(x,y):
    gameDisplay.blit(GPSImg, (x,y))

x =  (display_width * 0.45)
y = (display_height * 0.8)

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
		
		if click[0] == 1 and action != None:
			
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
		
		if click[0] == 1 and action != None:
			
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
	
def Load():
	load = True
	load = False
def mainScreen():
	main = True
	while main:
		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
        
		gameDisplay.fill(darkblue)
		largeText = pygame.font.Font('freesansbold.ttf',115)
		TextSurf, TextRect = text_objects("A bit Racey", largeText)
		TextRect.center = ((display_width/2),(display_height/2))
		gameDisplay.blit(TextSurf, TextRect)
		
		button("GO!",150,450,100,50,green,blue)
		button("Quit",550,450,100,50,red,black)
		GPSIcon(x,y)
		
		pygame.display.update()
		clock.tick(15)

Load()		
mainScreen()
pygame.quit()
quit()