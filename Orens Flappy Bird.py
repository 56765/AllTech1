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




def everything():
    time.sleep(1)
    bn=350
    x=400
    y=400
    yc=1
    nb=350


    vb=0
    bv=750


        
    yr=random.randint(550,800)
    xr=random.randint(0,450)
    def pipes():
        pygame.draw.rect(screen,green,(nb,vb,50,xr))
        pygame.draw.rect(screen,green,(bn,bv,50,yr))
    while True:
        pygame.draw.rect(screen,green,(nb,0,50,xr))
        pygame.draw.rect(screen,green,(bn,750,50,yr))
        
        pygame.draw.circle(screen,yellow,(x,y),25)
        for event in pygame.event.get():
          
            if event.type==KEYDOWN:
                yc=-2    

            if event.type==KEYUP:
                yc=1
        y=y+yc

        bn=bn-5
        nb=nb-5
     
        if nb==0 and bn==0:
            nb=850
            bn=850
            yr=random.randint(550,800)
            xr=random.randint(0,450)
        if y<=0 or y>=800:
            everything()
everything()
            
pygame.display.update()
screen.fill(black)

    
    
    
    
