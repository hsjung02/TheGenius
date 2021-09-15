#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import random
pygame.init()
temp=random.sample(range(0, 27), 9)
board=[]
for i in temp:
    board.append((i//9+1,(i%9)//3+1,(i%9)%3+1))
print(board)

def hap(a,b,c):
    if a==b and b==c:
        return True
    elif a!=b and b!=c and c!=a:
        return True
    else:
        return False
    
haplist=[]
for i in range(0,7):
    for j in range(i+1,8):
        for k in range(j+1,9):
            if hap(board[i][0],board[j][0],board[k][0]) and hap(board[i][1],board[j][1],board[k][1]) and hap(board[i][2],board[j][2],board[k][2]):
                haplist.append((i+1,j+1,k+1))
                
print(haplist)

spotlist=[(240*(i%3)+50,240*(i//3)+50) for i in range(9)]

imglist=[]
numlist=[]

anslist=[]

rounds=1
gyeolbutton=pygame.image.load('button/결.png')
passbutton=pygame.image.load('button/넘김.png')

score1=0
score2=0
turn=1

def showscore():
    global score1,score2,background,turn
    font = pygame.font.Font('arial.ttf',30)  #폰트 설정
    te = font.render('Player1: '+str(score1),True,(28,0,0),(91,155,213)) #91,155,213
    background.blit(te,(900,60))  
    font = pygame.font.Font('arial.ttf',30)  #폰트 설정
    tex = font.render('Player2: '+str(score2),True,(28,0,0),(91,155,213)) #91,155,213
    background.blit(tex,(1150,60))
    if turn==1:
        gamepad.blit(pygame.image.load('turn.png'),(900,100))
    else:
        gamepad.blit(pygame.image.load('turn.png'),(1150,100))     
        
def showans():
    global anslist,background
    for i in range(len(anslist)):
        font = pygame.font.Font('arial.ttf',30)
        background.blit(font.render(str(anslist[i][0])+'     '+str(anslist[i][1])+'     '+str(anslist[i][2]),True,(28,0,0),(91,155,213)),(830,200+i*40))


def newboard():
    global haplist,board,rotn,anslist
    temp=random.sample(range(0, 27), 9)
    board=[]
    for i in temp:
        board.append((i//9+1,(i%9)//3+1,(i%9)%3+1))
        haplist=[]
    for i in range(0,7):
        for j in range(i+1,8):
            for k in range(j+1,9):
                if hap(board[i][0],board[j][0],board[k][0]) and hap(board[i][1],board[j][1],board[k][1]) and hap(board[i][2],board[j][2],board[k][2]):
                    haplist.append((i+1,j+1,k+1))
    anslist=[]
    print(haplist,anslist)
    return

def showkan():
    for i in range(8):
        gamepad.blit(pygame.image.load('kan.png'),(800,200+i*86))


def getimg(board):
    a=[]
    ident=''
    for i in board:
        ident=str(i[0])+str(i[1])+str(i[2])
        a.append(pygame.image.load('img/'+ident+'.png'))
    return a

def getnum():
    global numlist
    for i in range(1,10):
        numlist.append(pygame.image.load('num/'+str(i)+'.png'))
    return

def findspot(x,y):
    global spotlist
    temp = []
    for i in spotlist:
        temp.append((i[0]+120-x)**2+(i[1]+120-y)**2)
    return temp.index(min(temp))
        
def correct():
    global right,error
    if right==1 and error==0:
        gamepad.blit(pygame.image.load('button/정답.png'),(1080,250))
    elif right==0 and error==1:
        gamepad.blit(pygame.image.load('button/오답.png'),(1080,250))
    elif right==0 and error==0:
        gamepad.blit(pygame.image.load('button/null.png'),(1080,250))
    
def placeimg():
    global spotlist,imglist,numlist
    for i in range(9):
        gamepad.blit(imglist[i],spotlist[i])
        gamepad.blit(numlist[i],spotlist[i])
    return

def showbutton():
    global gyeolbutton,passbutton,rounds
    gamepad.blit(gyeolbutton,(1080,500))
    gamepad.blit(passbutton,(1080,750))
    font = pygame.font.Font('arial.ttf',80)  #폰트 설정
    tex = font.render('ROUND '+str(rounds),True,(28,0,0),(91,155,213)) #91,155,213
    background.blit(tex,(900,60))

def check(a,b,c):
    global haplist
    if (a,b,c) in haplist:
        return True
    else:
        return False
    
def back(x,y):
    global gamepad, background
    gamepad.blit(background,(x,y))
    
    
def ansclear():
    for i in range(20):
        font = pygame.font.Font('arial.ttf',40)  #폰트 설정
        tex = font.render('                                 ',True,(28,0,0),(91,155,213)) #91,155,213
        background.blit(tex,(820,200+i*40))

WHITE=(255,255,255)
pad_width =1350
pad_height = 1000

spot1=-1
spot2=-1
spot3=-1
gyeol=0
right=0
error=0

imglist=getimg(board)
getnum()
def runGame():
    global gamepad,clock,background,spot1,spot2,spot3,imglist,board,haplist,temp,imglist,anslist,right,error,rounds
    flag=True
    while flag:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                flag=False
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if 50<pygame.mouse.get_pos()[0]<770 and 50<pygame.mouse.get_pos()[1]<770:
                    if spot1==-1:
                        spot1=findspot(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                    elif spot1!=-1 and spot2==-1:
                        spot2=findspot(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                    elif spot2!=-1 and spot3==-1:
                        spot3=findspot(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                elif 1080<pygame.mouse.get_pos()[0]<1320 and 500<pygame.mouse.get_pos()[1]<590:
                    if haplist==[]:
                        right=1
                        error=0
                        font = pygame.font.Font('arial.ttf',40)
                        background.blit(font.render('GYEOL',True,(28,0,0),(91,155,213)),(830,200+len(anslist)*40))
                        gyeol=1
                    else:
                        right=0
                        error=1
                        spot1=-1
                        spot2=-1
                        spot3=-1
                elif 1080<pygame.mouse.get_pos()[0]<1320 and 750<pygame.mouse.get_pos()[1]<990 and gyeol==1:
                    rounds+=1
                    newboard()
                    ansclear()
                    imglist=getimg(board)
                    gyeol=0
                    
        if spot3!=-1:
            if check(spot1+1,spot2+1,spot3+1):
                haplist.remove((spot1+1,spot2+1,spot3+1))
                anslist.append((spot1+1,spot2+1,spot3+1))
                right=1
                error=0
                print(spot1+1,spot2+1,spot3+1)
                print(haplist,anslist)
                spot1=-1
                spot2=-1
                spot3=-1
            else:
                right=0
                error=1
                spot1=-1
                spot2=-1
                spot3=-1
                
        back(0,0)
        showans()
        correct()
        showbutton()
        placeimg()
        pygame.display.update()
        clock.tick(10)
    pygame.quit()

def initGame():
    global gamepad, clock,background

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width,pad_height))
    pygame.display.set_caption('결!합!')
    background = pygame.image.load("background.png")
    clock=pygame.time.Clock()
    runGame()
    
initGame()


# In[ ]:





# In[ ]:





# In[ ]:




