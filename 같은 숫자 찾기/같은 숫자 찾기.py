#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pygame
import random
pygame.init()
alpha=random.sample(range(1, 27), 16)
num=[i for i in range(1,17)]
random.shuffle(num)
alphaimg=[]
numimg=[]
start=0
qnum=0
sign=0
for i in alpha:
    alphaimg.append(pygame.image.load('alphabet/'+str(i)+'.png'))
for i in num:
    numimg.append(pygame.image.load('number/'+str(i)+'.png'))
buttonimg=[pygame.image.load('button/start.png'),pygame.image.load('button/reset.png')]
signimg=[pygame.image.load('sign/기본.png'),pygame.image.load('sign/정답.png'),pygame.image.load('sign/오답.png')]
nextimg=[pygame.image.load('next/기본.png'),pygame.image.load('next/next.png'),pygame.image.load('next/기본.png')]
smallbg=pygame.image.load('smallbg.png')

numdic={1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'11',12:'12',13:'+',14:'-',15:'*',16:'/'}
questions=[10,20,21,110,24,12,2,108,11,16,72,90,8,3,4,5,6,7,8,9,13,55,13,5,17,42,15]
random.shuffle(questions)
question=questions[:14]

spotlist=[(200*(i%4)+100,200*(i//4)+50) for i in range(16)]


def findspot(x,y):
    global spotlist
    temp = []
    for i in spotlist:
        temp.append((i[0]+120-x)**2+(i[1]+120-y)**2)
    return temp.index(min(temp))
    
def placepiece():
    global spotlist, alphaimg,numimg,buttonimg,signimg,sign,nextimg
    for i in range(16):
        if i==spot1:
            gamepad.blit(numimg[spot1],(spotlist[spot1][0],spotlist[spot1][1]))
        elif i==spot2:
            gamepad.blit(numimg[spot2],(spotlist[spot2][0],spotlist[spot2][1]))
        elif i==spot3:
            gamepad.blit(numimg[spot3],(spotlist[spot3][0],spotlist[spot3][1]))
        else:
            gamepad.blit(alphaimg[i],(spotlist[i][0],spotlist[i][1]))
    gamepad.blit(buttonimg[0],(1000,400))
    gamepad.blit(buttonimg[1],(1000,525))
    gamepad.blit(signimg[sign],(1030,300))
    gamepad.blit(nextimg[sign],(1000,650))
    
def placenum():
    global spotlist,numimg,buttonimg,signimg,sign
    for i in range(16):
        gamepad.blit(numimg[i],(spotlist[i][0],spotlist[i][1]))
    gamepad.blit(buttonimg[0],(1000,400))
    gamepad.blit(buttonimg[1],(1000,525))
    gamepad.blit(signimg[sign],(1030,300))
    gamepad.blit(nextimg[sign],(1000,650))

def showquestion(qnum):
    global question
    font = pygame.font.Font('arial.ttf',70)  #폰트 설정
    te = font.render(str(qnum+1)+'/'+str(len(question)),True,(28,0,0),(91,155,213)) #91,155,213
    background.blit(te,(1050,60))  
    font = pygame.font.Font('arial.ttf',100)  #폰트 설정
    tex = font.render('           ',True,(28,0,0),(91,155,213)) #91,155,213
    background.blit(tex,(1050,150))  
    font = pygame.font.Font('arial.ttf',100)  #폰트 설정
    text = font.render(str(question[qnum]),True,(28,0,0),(91,155,213)) #91,155,213
    background.blit(text,(1050,150))  
    
WHITE=(255,255,255)
pad_width =1350
pad_height = 1000

spot1=-1
spot2=-1
spot3=-1

def back(x,y):
    global gamepad, background
    gamepad.blit(background,(x,y))
    
def anscheck(qnum):
    global question,spot1,spot2,spot3,num,numdic
    try:
        return question[qnum]==eval(numdic[num[spot1]]+numdic[num[spot2]]+numdic[num[spot3]])
    except SyntaxError:
        return False

def runGame():
    global gamepad,clock,background,spot1,spot2,spot3,start,qnum,sign,smallbg
    flag=True
    while flag:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                flag=False
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if 100<pygame.mouse.get_pos()[0]<900 and 50<pygame.mouse.get_pos()[1]<850:
                    if spot1==-1:
                        spot1=findspot(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                    elif spot1!=-1 and spot2==-1:
                        spot2=findspot(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                    elif spot1!=-1 and spot2!=-1 and spot3==-1:
                        spot3=findspot(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                    if spot1!=-1 and spot2!=-1 and spot3!=-1:
                        check=anscheck(qnum)
                        if check==True:
                            sign=1
                        else:
                            sign=2
                elif 1000<pygame.mouse.get_pos()[0]<1266 and 400<pygame.mouse.get_pos()[1]<500:
                    start=1
                elif 1000<pygame.mouse.get_pos()[0]<1266 and 525<pygame.mouse.get_pos()[1]<625:
                    spot1=-1
                    spot2=-1
                    spot3=-1
                elif 1000<pygame.mouse.get_pos()[0]<1266 and 650<pygame.mouse.get_pos()[1]<750:
                    if sign==1:
                        qnum+=1
                        sign=0
                        spot1=-1
                        spot2=-1
                        spot3=-1
                        gamepad.blit(smallbg,(1000,125))
        gamepad.fill(WHITE)
        back(0,0)
        if start==0:
            placenum()
        else:
            placepiece()
            showquestion(qnum)
        pygame.display.update()
        clock.tick(10)
    pygame.quit()

def initGame():
    global gamepad, clock,background

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width,pad_height))
    pygame.display.set_caption('같은 숫자 찾기')
    clock=pygame.time.Clock()
    background = pygame.image.load("background.png")
    runGame()
    
initGame()


# In[ ]:





# In[ ]:





# In[ ]:




