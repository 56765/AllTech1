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
score=0


def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont('freesans',32)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))


def everything():
    time.sleep(1)
    bn=350
    x=400
    y=400
    yc=1
    nb=350


    vb=0
    bv=750


    tep=random.randint(500,800) 
    yr=random.randint(550,800)
    xr=random.randint(0,450)
    tim=time.time()
    while True:
        screen.fill(black)
        
      

      
        

      
        tep=random.randint(500,800)
        xr=random.randint(0,450)
        pygame.draw.rect(screen,yellow,(nb,0,25,xr+25))
        pygame.draw.rect(screen,red,(nb-30,0,25,xr+25))
        pygame.draw.rect(screen,yellow,(bn,tep+25,25,yr))
        pygame.draw.rect(screen,red,(bn-35,tep+25,25,yr))
        pygame.draw.rect(screen,yellow,(nb+30,0,25,xr+25))
        pygame.draw.rect(screen,red,(bn+30,tep,25,yr))
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
            
            
        if y<=0 or y>=800:
            everything()
        if x+25==nb and y in range(0,10):
            everything()
##        show_text(blah,750,50,blue)
        cor=time.time()-tim
        cor = int(cor)
        show_text(str(cor), 750,50, blue)
        if((x+50==bn)) and ((y>yr and y<yr+xr)):
            print("Collision")
            everything()

            
        pygame.display.update()

        
everything()  
            

   

    
    
    
    
