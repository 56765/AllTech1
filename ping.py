import time
import random
import pygame
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption('Animation')
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
color=(255,0,0)
x=400
y=400

xchange1=1
ychange1=1

class Ball:
    def __init__(self,x,y,color,radius):
        self.x=x
        self.y=y
        self.color=color
        self.radius=radius
    def move(self,xchange,ychange):
        self.x=self.x+xchange
        self.y=self.y+ychange
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
        
    
    
        

        
    
b1=Ball(1,2,red,50)    

 
        
while True:

    b1.move(xchange1,ychange1)

    b1.draw()

    pygame.display.update()
    screen.fill(black)



 
        
        


