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
a = ["magic1.png", "Magic2.png", "magic3.png", "magic4.png", "magic5.png"]
f = ["magic_f_1.png", "f2.png", "f3.png", "f4.png", "f5.png"]
key=""
k=0
while True:
        pygame.display.update()
        screen.fill(black)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            elif event.type==KEYDOWN:
                if event.key==K_n:
                       key='n'
       
                        
                   

                
                if event.key==K_d:
                         key='d'
        
                if event.key==K_a :
                    x=x-25
                    img=pygame.image.load(f[k])
                    screen.blit(img,(x, y))
##                    pygame.display.update()
##                    screen.fill(black)
                    time.sleep(0.1)
                    k=k+1
                    if k==5:
                        k=0
                if event.key==K_w :
                    y=y-25
                    img=pygame.image.load(f[k])
                    screen.blit(img,(x, y))
##                    pygame.display.update()
##                    screen.fill(black)
                    time.sleep(0.1)
                    k=k+1
                    if k==5:
                        k=0
                if event.key==K_s :
                    y=y+25
                    img=pygame.image.load(f[k])
                    screen.blit(img,(x, y))
##                    pygame.display.update()
##                    screen.fill(black)
                    time.sleep(0.1)
                    k=k+1
                    if k==5:
                        k=0
                if event.key==K_k:
                    y=y-200
                    img=pygame.image.load(f[k])
                    screen.blit(img,(x, y))
##                    pygame.display.update()
##                    screen.fill(black)
                    time.sleep(0.1)
                    time.sleep(0.3)
                    k=k+1
                    if k==5:
                        k=0
                    y=y+200
                    img=pygame.image.load(f[k])
                    screen.blit(img,(x, y))
##                    pygame.display.update()
##                    screen.fill(black)
                    time.sleep(0.1)
                    k=k+1
                    if k==5:
                        k=0
                
       
        if key=="n":
            img=pygame.image.load('bullet.png')
            screen.blit(img,(x,y-5))
            pygame.display.update()
                        
            k=k+1
            if k==5:
                k==0

        if key=="d":
            x=x+25
            img=pygame.image.load(a[k])
            screen.blit(img,(x, y))
##                    pygame.display.update()
##                    screen.fill(black)
            time.sleep(0.1)
            k=k+1
            if k==5:
                k=0


       
             











