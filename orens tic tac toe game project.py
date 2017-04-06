import time
import pygame
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption('Tic Tac Toe')
red=(255,0,0)
x=0
y=0
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
d=0
def show_text(msg,x,y,color):
        fontobj=pygame.font.SysFont('freesans',50)
        msgobj=fontobj.render(msg,False,color)
        screen.blit(msgobj,(x,y))
def menu():
        time.sleep(3)
        screen.fill(black)
        global x,y

        while True:
                pygame.draw.rect(screen,red,(50,200,200,200))
                pygame.draw.rect(screen,red,(350,200,200,200))
                pygame.display.update()
                for event in pygame.event.get():
                        if event.type==QUIT:
                            pygame.quit()
                            exit()
                        elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                            print(event.pos)
                            x,y=event.pos
                    
     
                show_text('Play',100,250,green)
                show_text('Quit',400,250,green)
                if x in range(50,250) and y in range(200,400):
                        print('playClicked')
                        game()

                        
                elif x in range(350,550) and y in range(200,400):
                        quit()
                pygame.display.update()
                
def game():
        screen.fill(black)
        pygame.draw.line(screen,white,(200,0),(200,600))
        pygame.draw.line(screen,white,(400,0),(400,600))
        pygame.draw.line(screen,white,(0,200),(600,200))
        pygame.draw.line(screen,white,(0,400),(600,400))


        def X1():
                pygame.draw.line(screen,white,(0,200),(200,0))
                pygame.draw.line(screen,white,(200,200),(0,0))
        def X2():
                pygame.draw.line(screen,white,(200,0),(400,200))
                pygame.draw.line(screen,white,(400,0),(200,200))
        def X3():
                pygame.draw.line(screen,white,(400,0),(600,200))
                pygame.draw.line(screen,white,(600,0),(400,200))        
        def X4():
                pygame.draw.line(screen,white,(200,200),(0,400))
                pygame.draw.line(screen,white,(0,200),(200,400))
        def X5():
                pygame.draw.line(screen,white,(200,400),(400,200))
                pygame.draw.line(screen,white,(200,200),(400,400))
        def X6():
                pygame.draw.line(screen,white,(400,400),(600,200))
                pygame.draw.line(screen,white,(400,200),(600,400))
        def X7():
                pygame.draw.line(screen,white,(0,600),(200,400))
                pygame.draw.line(screen,white,(0,400),(200,600))
        def X8():
                pygame.draw.line(screen,white,(200,400),(400,600))
                pygame.draw.line(screen,white,(200,600),(400,400))
        def X9():
                pygame.draw.line(screen,white,(400,600),(600,400))
                pygame.draw.line(screen,white,(400,400),(600,600))
        def C1():
                pygame.draw.circle(screen,white,(100,100),100,1)
        def C2():
                pygame.draw.circle(screen,white,(300,100),100,1)
        def C3():
                pygame.draw.circle(screen,white,(500,100),100,1)
        def C4():
                pygame.draw.circle(screen,white,(100,300),100,1)
        def C5():
                pygame.draw.circle(screen,white,(300,300),100,1)
        def C6():
                pygame.draw.circle(screen,white,(500,300),100,1)
        def C7():
                pygame.draw.circle(screen,white,(100,500),100,1)
        def C8():
                pygame.draw.circle(screen,white,(300,500),100,1)
        def C9():
                pygame.draw.circle(screen,white,(500,500),100,1)
        def cw():
                if d[1]==d[2]==d[3]=='x' or d[4]==d[5]==d[6]=='x' or d[7]==d[8]==d[9]=='x' or d[1]==d[4]==d[7]=='x' or d[2]==d[5]==d[8]=='x' or d[3]==d[6]==d[9]=='x' or d[1]==d[5]==d[9]=='x':
                        print('x wins')
                        show_text('X Wins',268,268,blue)
                        pygame.display.update()
                        menu()
##                      menu()
                        return        
                elif d[1]==d[2]==d[3]=='o' or d[4]==d[5]==d[6]=='o' or d[7]==d[8]==d[9]=='o' or d[1]==d[4]==d[7]=='o' or d[2]==d[5]==d[8]=='o' or d[3]==d[6]==d[9]=='o' or d[1]==d[5]==d[9]=='o':
                        print('O wins')
                        show_text('O Wins',268,268,blue)
                        pygame.display.update()
                        menu()
                elif d[1] !="_" and d[2] !="_" and d[3] !="_" and d[4] !="_" and d[5] !="_" and d[6] !="_" and d[7] !="_" and d[8] !="_" and d[9] !="_":
                        print('draw')
                        show_text('Draw',268,268,blue)
                        pygame.display.update()
                        menu()
                

               
                



        d={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
        player=0

        while True:
            pygame.display.update()
            cw()
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    print(event.pos)
                    x,y=event.pos
                    if x in range(0,200) and y in range(0,200):
                        if player==0 and d[1]=='_':
                            X1()
                            player=1
                            d[1]='x'
                        elif player==1 and d[1]=="_":
                            C1()
                            player=0
                            d[1]='o'

                    if x in range(200,400) and y in range(0,200):
                        if player==0 and d[2]=='_':
                            X2()
                            player=1
                            d[2]='x'
                        elif player==1 and d[2]=="_":
                            C2()
                            player=0
                            d[2]='o'

                        
                        
                   
                    if x in range(400,600) and y in range(0,200):
                        if player==0 and d[3]=='_':
                            X3()
                            player=1
                            d[3]='x'
                        elif player==1 and d[3]=="_":
                            C3()
                            player=0
                            d[3]='o'


                    if x in range(0,200) and y in range(200,400):
                        if player==0 and d[4]=='_':
                            X4()
                            player=1
                            d[4]='x'
                        elif player==1 and d[4]=="_":
                            C4()
                            player=0
                            d[4]='o'


                    if x in range(200,400) and y in range(200,400):
                        if player==0 and d[5]=='_':
                            X5()
                            player=1
                            d[5]='x'
                        elif player==1 and d[5]=="_":
                            C5()
                            player=0
                            d[5]='o'


                    if x in range(400,600) and y in range(200,400):
                        if player==0 and d[6]=='_':
                            X6()
                            player=1
                            d[6]='x'
                        elif player==1 and d[6]=="_":
                            C6()
                            player=0
                            d[6]='o'


                    if x in range(0,200) and y in range(400,600):
                        if player==0 and d[7]=='_':
                            X7()
                            player=1
                            d[7]='x'
                        elif player==1 and d[7]=="_":
                            C7()
                            player=0
                            d[7]='o'


                    if x in range(200,400) and y in range(400,600):
                        if player==0 and d[8]=='_':
                            X8()
                            player=1
                            d[8]='x'
                        elif player==1 and d[8]=="_":
                            C8()
                            player=0
                            d[8]='o'


                    if x in range(400,600) and y in range(400,600):
                        if player==0 and d[9]=='_':
                            X9()
                            player=1
                            d[9]='x'
                        elif player==1 and d[9]=="_":
                            C9()
                            player=0
                            d[9]='o'
menu()
                            


                                
            
        
            
            
        
            
        
