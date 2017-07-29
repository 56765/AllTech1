import time
import random
import pygame
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption('animation11')
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=((0,0,0))
yellow=(255,240,6)
x=400
y=400

walk=['Walk1.png','Walk2.png','walk3.png']

while True:
    img=pygame.image.load("cat.png")
    screen.blit(img,(x, y))
    pygame.display.update()
##    for i in walk:
##        #screen.fill(black)
##        print(i)
##        img=pygame.image.load(i)
##        screen.blit(img,(x, y))
##        x-=10             #x=x-10
##        pygame.display.update()
##        time.sleep(0.5)
##        
