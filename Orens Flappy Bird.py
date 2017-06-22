import time
import random
import pygame
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption('Flappy Bird')
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
yellow=(255,240,6)
x=400
y=400
yc=1
yr=random.randint(550,800)
xr=random.randint(0,450)
while True:
    
    pygame.draw.circle(screen,yellow,(x,y),25)
    for event in pygame.event.get():
      
        if event.type==KEYDOWN:
            yc=-2    

        if event.type==KEYUP:
            yc=1
    y=y+yc
    pygame.draw.rect(screen,green,(350,0,50,xr))
    pygame.draw.rect(screen,green,(350,750,50,yr))

     




    pygame.display.update()
    screen.fill(black)
    
    
    
