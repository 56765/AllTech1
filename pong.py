
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

xc=random.randint(1,10)
yc=random.randint(1,10)
v=0
vc=500
lc=0
l=500
fpsclock=pygame.time.Clock()
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
color=(255,0,0)
aa=0
oo=0
ww=0
ss=0
ll=0
xp=750
yp=0
benny=0
timmy=0
def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("freesans",32)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
        
while True:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
             if event.key == K_l:
                aa=1
             if event.key == K_o:
                 oo=1
             if event.key == K_s:
                 ss=1
             if event.key == K_w:
                 ww=1
        if event.type==KEYUP:
             if  event.key==K_l:
                aa=0
             if event.key==K_o:
##                 print('hi')
                 oo=0
             if  event.key==K_s:
                ss=0
             if event.key==K_w:
                 ww=0
    if aa==1 and ll<600:
        ll=ll+2
    if oo==1 and ll>0:
        ll=ll-2
    if ss==1 and vc<600:
        vc=vc+2
    if ww==1 and vc>0:
        vc=vc-2
    if x >900 :
        x=400
        y=400
        benny=benny+1
    show_text(str(benny),100,700,white)
    if x<0:
        x=400
        y=400
        timmy=timmy+1
    show_text(str(timmy),100,700,white)
        
       



    pygame.draw.circle(screen,blue,(x,y),50)
    x+=xc
    y+=yc
    if x>=700 and ll<=y<=ll+200:
       xc=-random.randint(1,2)
    if x<=100 and vc<=y<=vc+200:
        xc=random.randint(1,2)
    if y>=750:
        yc=-random.randint(1,2)
    if y<=50:
       yc=random.randint(1,2)


    pygame.draw.rect(screen,green,(xp,ll,50,200))
    pygame.draw.rect(screen,red,(yp,vc,50,200))
    
    pygame.display.update()
    

        
        


