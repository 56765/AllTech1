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
x=100
y=100



while True:
    img=pygame.image.load("magic1.png")
    screen.blit(img,(x, y))
    pygame.display.update()
    screen.fill(black)
    time.sleep(0.1)

    img=pygame.image.load("Magic2.png")
    screen.blit(img,(x,y ))
    pygame.display.update()
    screen.fill(black)
    time.sleep(0.1)

    img=pygame.image.load("magic3.png")
    screen.blit(img,(x,y ))
    pygame.display.update()
    screen.fill(black)
    time.sleep(0.1)

    
    img=pygame.image.load("magic4.png")
    screen.blit(img,(x,y ))
    pygame.display.update()
    screen.fill(black)
    time.sleep(0.1)

        
    img=pygame.image.load("magic5.png")
    screen.blit(img,(x,y ))
    pygame.display.update()
    screen.fill(black)
    time.sleep(0.1)













