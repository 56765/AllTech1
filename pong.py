import time
import pygame
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption('Animation')
red=(255,0,0)
x=300
y=300
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
while True:
    pygame.display.update()
    pygame.draw.circle(screen,blue,(x,y),50)
    while True:
        x=x+1
    if x==550:
        while True:
            x=x-1
    if x==50:
        x=x+1
        

    
