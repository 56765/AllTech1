import time
import random
import pygame
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption('Animation')
red=(255,0,0)
x=300
y=300
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
fx=0
fy=0
xc=random.randint(1,10)
yc=random.randint(1,10)

snowlist=[]
for i in range(100):
    a=[random.randint(0,800), random.randint(0,800)]
    snowlist.append(a)
print(snowlist)
    

while True:
    pygame.display.update()
    screen.fill(black)
    for sdf in range(100):
        pygame.draw.circle(screen,blue,(snowlist[sdf]),2)
        snowlist[sdf][1]=snowlist[sdf][1]+1

    
    


##while True:
##    pygame.display.update()
##    screen.fill(black)
##    pygame.draw.circle(screen,blue,(x,y),50)
##    x+=xc
##    y+=yc
##    if x>=750:
##        xc=-random.randint(1,5)
##    if y>=550:
##        yc=-random.randint(1,5)
##    if x<=0:
##        xc=random.randint(1,5)
##    if y<=0:
##        yc=random.randint(1,5)


