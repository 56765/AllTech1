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
yellow=(255,255,0)
orange= (0,255,255)

purple=(255,0,255)
x=400
y=400
pr=0
pl=0
xchange1=2
ychange1=3
xchange2=2
ychange2=2
xchange3=3
ychange3=2

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


class Paddles:
    def __init__(self,x,y,color,length,width):
        self.x=x
        self.y=y
        self.color=color
        self.width=width
        self.length=length
    def move(self,ychange):
        self.y=self.y+ychange
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.length))


        

        
    
b1=Ball(400,400,red,50)
b2=Ball(400,500,yellow,50)
b3=Ball(400,300,orange,50)
p1=Paddles(0,300,green,200,50)
p2=Paddles(750,300,purple,200,50)

 
        
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()

        if event.type==KEYDOWN:
            if event.key==K_w:
                pr=-1
            if event.key==K_s:
                pr=1
            if event.key==K_UP:
                pl=-1
            if event.key==K_DOWN:
                pl=1
                   

    

    b1.move(xchange1,ychange1)
    b2.move(xchange2,ychange2)
    b3.move(xchange3,ychange3)
    b1.draw()
    b2.draw()
    b3.draw()
    p1.draw()
    p2.draw()
    
    pygame.display.update()
    screen.fill(black)
    if b1.x>750 or b1.x<50:
        xchange1=-xchange1
    if b1.y>750 or b1.y<50:
        ychange1=-ychange1
    if b2.x>750 or b2.x<50:
        xchange2=-xchange2
    if b2.y>750 or b2.y<50:
        ychange2=-ychange2
    if b3.x>750 or b3.x<50:
        xchange3=-xchange3
    if b3.y>750 or b3.y<50:
        ychange3=-ychange3
    if p1.y>800:
        p1.y=p1.y-1
    if p1.y<50:
        p1.y=p1.y+1

    if p2.y>800:
        p2.y=p2.y-1
    if p2.y<50:
        p2.y=p2.y+1
    
            
            
    if b1.x in range(b2.x-50,b2.x+50) and b1.y in range(b2.y-50,b2.y+50):
        xchange1=-xchange1
        ychange1=-ychange1
        xchange2=-xchange2
        ychange2=-ychange2

    if b2.x in range(b3.x-50,b3.x+50) and b2.y in range(b3.y-50,b3.y+50):
        xchange3=-xchange3
        ychange3=-ychange3
        xchange2=-xchange2
        ychange2=-ychange2

    if b3.x in range(b1.x-50,b1.x+50) and b3.y in range(b1.y-50,b1.y+50):
        xchange3=-xchange3
        ychange3=-ychange3
        xchange1=-xchange1
        ychange1=-ychange1

    
    


    





 
        
        


