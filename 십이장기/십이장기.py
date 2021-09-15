#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
pygame.init()
WHITE=(255,255,255)
pad_width =1440
pad_height = 1280
fromspot=-1
tospot=-1
movingpiece=0
diepiece=0
hand1toboard=-1
hand2toboard=-1
hand1board=-1
hand2board=-1

class piece():
    def __init__(self,typ,spot,position,moving):
        self.typ=typ
        self.position = position
        self.spot_x = spot[0]
        self.spot_y = spot[1]
        self.moving=moving
    
    def image(self):
        if self.typ=='a' and self.position==1:
            self.img = pygame.image.load("img/자1.png")
        elif self.typ=='a' and self.position==2:
            self.img = pygame.image.load("img/자2.png")
        elif self.typ=='b' and self.position==1:
            self.img = pygame.image.load("img/상1.png")
        elif self.typ=='b' and self.position==2:
            self.img = pygame.image.load("img/상2.png")
        elif self.typ=='c' and self.position==1:
            self.img = pygame.image.load("img/장1.png")
        elif self.typ=='c' and self.position==2:
            self.img = pygame.image.load("img/장2.png")
        elif self.typ=='d' and self.position==1:
            self.img = pygame.image.load("img/후1.png")
        elif self.typ=='d' and self.position==2:
            self.img = pygame.image.load("img/후2.png")
        elif self.typ=='e' and self.position==1:
            self.img = pygame.image.load("img/왕1.png")
        elif self.typ=='e' and self.position==2:
            self.img = pygame.image.load("img/왕2.png")
        
    def loadhand1img(self):
        if self.typ=='a':
            self.img = pygame.image.load("hand/자1.png")
        elif self.typ=='b':
            self.img = pygame.image.load("hand/상1.png")
        elif self.typ=='c':
            self.img = pygame.image.load("hand/장1.png")
        elif self.typ=='d':
            self.img = pygame.image.load("hand/후1.png")
            
    def loadhand2img(self):
        if self.typ=='a':
            self.img = pygame.image.load("hand/자2.png")
        elif self.typ=='b':
            self.img = pygame.image.load("hand/상2.png")
        elif self.typ=='c':
            self.img = pygame.image.load("hand/장2.png")
        elif self.typ=='d':
            self.img = pygame.image.load("hand/후2.png")
            
    def legalmove(self,fromspot,tospot):
        if self.typ=='a' and self.position==1:
            if tospot==fromspot+3:
                if tospot//3==3:
                    self.typ='d'
                return True
            else:
                return False
        elif self.typ=='a' and self.position==2:
            if tospot==fromspot-3:
                if tospot//3==0:
                    self.typ='d'
                return True
            else:
                return False
        elif self.typ=='b':
            if abs(tospot%3-fromspot%3)==1 and abs(tospot//3-fromspot//3)==1:
                return True
            else:
                return False
        elif self.typ=='c':
            if abs(tospot-fromspot)==1 and tospot//3==fromspot//3:
                return True
            elif tospot%3==fromspot%3 and abs(tospot-fromspot)==3:
                return True
            else:
                return False
        elif self.typ=='d' and self.position==1:
            if tospot-fromspot==-3:
                return False
            elif abs(tospot-fromspot)==1 and tospot//3==fromspot//3:
                return True
            elif tospot%3==fromspot%3 and abs(tospot-fromspot)==3:
                return True 
            elif abs(tospot%3-fromspot%3)==1 and abs(tospot//3-fromspot//3)==1:
                return True
            else:
                return False
        elif self.typ=='d' and self.positon==2:
            if tospot-fromspot==3 and tospot//3==fromspot//3:
                return False
            elif abs(tospot-fromspot)==1 and tospot//3==fromspot//3:
                return True
            elif tospot%3==fromspot%3 and abs(tospot-fromspot)==3:
                return True 
            elif abs(tospot%3-fromspot%3)==1 and abs(tospot//3-fromspot//3)==1:
                return True
            else:
                return False
        elif self.typ=='e':
            if abs(tospot-fromspot)==1 and tospot//3==fromspot//3:
                return True
            elif tospot%3==fromspot%3 and abs(tospot-fromspot)==3:
                return True 
            elif abs(tospot%3-fromspot%3)==1 and abs(tospot//3-fromspot//3)==1:
                return True
            else:
                return False
            

spotlist = [(17,17),(17,262),(17,507),(262,17),(262,262),(262,507),(507,17),(507,262),(507,507),(752,17),(752,262),(752,507)]
ja1=piece('a',spotlist[4],1,0) #0
ja2=piece('a',spotlist[7],2,0)  #1
sang1=piece('b',spotlist[0],1,0) #2
sang2=piece('b',spotlist[11],2,0)  #3
jang1=piece('c',spotlist[2],1,0)  #4
jang2=piece('c',spotlist[9],2,0)  #5
king1=piece('e',spotlist[1],1,0)  #6
king2=piece('e',spotlist[10],2,0)  #7

piecelist=[ja1,ja2,sang1,sang2,jang1,jang2,king1,king2]
board=[2,6,4,-1,0,-1,-1,1,-1,5,7,3]
p={0:'ja1',1:'ja2',2:'sang1',3:'sang2',4:'jang1',5:'jang2',6:'king1',7:'king2',-1:'empty'}
hand1 = []
hand2 = []

def back(x,y):
    global gamepad, background
    gamepad.blit(background,(x,y))
    
    
def showboard():
    global board,p
    for i in range(3):
        for j in range(4):
            print("%5s"%p[board[i+3*j]], end='  ')
        print('\n')
    
def placepiece():
    global gamepad, piecelist,spotlist,hand1,hand2
    for i in piecelist:
        i.image()
        if piecelist.index(i) in hand2:
            if i.moving==1:
                pass
            else:
                i.spot_x=1000-hand2.index(piecelist.index(i))*150
                i.spot_y=750
                i.loadhand2img()
        elif piecelist.index(i) in hand1:
            if i.moving==1:
                pass
            else:
                i.spot_x=hand1.index(piecelist.index(i))*150+17
                i.spot_y=750
                i.loadhand1img()
        
        gamepad.blit(i.img,(i.spot_x,i.spot_y))
    
        
def findspot(x,y):
    global spotlist
    temp = []
    for i in spotlist:
        temp.append((i[0]+120-x)**2+(i[1]+120-y)**2)
    return temp.index(min(temp))

def findhand1spot(x,y):
    global hand1
    spotlist=[17+i*150 for i in range(len(hand1))]
    temp=[]
    for i in spotlist:
        temp.append((i+62-x)**2)
    return temp.index(min(temp))

def findhand2spot(x,y):
    global hand2
    spotlist=[1000-150*i for i in range(len(hand2))]
    temp=[]
    for i in spotlist:
        temp.append((i+62-x)**2)
    return temp.index(min(temp))

def finishGame(winner):
    global gamepad, clock, background
    gamepad.fill(WHITE)
    fonto = pygame.font.Font('font/arial.ttf',30)  
    text = fonto.render("player %s wins"%winner,True,(28,0,0))  
    background.blit(text,(870,20))
    
def runGame():
    global gamepad, clock, background,piecelist,spotlist,board,fromspot,tospot,movingepiece,diepiece,hand1toboard,hand2toboard,hand1board,hand2board
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag=False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[1]<750 and pygame.mouse.get_pos()[0]<993:
                    fromspot=findspot(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                    movingpiece=board[fromspot]
                else:
                    if pygame.mouse.get_pos()[0]<len(hand1)*150+17 and pygame.mouse.get_pos()[1]>750:
                        hand1toboard=findhand1spot(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                        piecelist[hand1[hand1toboard]].moving=1
                    elif pygame.mouse.get_pos()[0]>1000-len(hand2)*150 and pygame.mouse.get_pos()[1]>750:
                        hand2toboard=findhand2spot(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                        piecelist[hand2[hand2toboard]].moving=1
            elif event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pos()[1]<750 and pygame.mouse.get_pos()[0]<993:
                    if hand1toboard==-1 and hand2toboard==-1:
                        tospot=findspot(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                        if fromspot==tospot and fromspot!=-1:
                            piecelist[movingpiece].spot_x=spotlist[fromspot][0]
                            piecelist[movingpiece].spot_y=spotlist[fromspot][1]
                            fromspot=-1
                            tospot=-1
                        else:
                            diepiece=board[tospot]
                    elif hand1toboard!=-1:
                        piecelist[hand1[hand1toboard]].image()
                        hand1board=findspot(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                        if board[hand1board]!=-1:
                            hand1toboard=-1
                            hand1board=-1
                            piecelist[hand1[hand1toboard]].moving=0
                    elif hand2toboard!=-1:
                        piecelist[hand2[hand2toboard]].image()
                        hand2board=findspot(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                        if board[hand2board]!=-1:
                            hand2toboard=-1
                            hand2board=-1
                            piecelist[hand2[hand2toboard]].moving=0
                else:
                    if hand1toboard==-1 and hand2toboard==-1:
                        piecelist[movingpiece].spot_x=spotlist[fromspot][0]
                        piecelist[movingpiece].spot_y=spotlist[fromspot][1]
                        fromspot=-1
                        tospot=-1
                    elif hand1toboard!=-1:
                        piecelist[hand1[hand1toboard]].moving=0
                        hand1toboard=-1
                    elif hand2toboard!=-1:
                        piecelist[hand2[hand2toboard]].moving=0
                        hand2toboard=-1
        if fromspot!=-1:
            piecelist[movingpiece].spot_x=pygame.mouse.get_pos()[0]-60
            piecelist[movingpiece].spot_y=pygame.mouse.get_pos()[1]-60
        if tospot!=-1:
            if piecelist[movingpiece].legalmove(fromspot,tospot):
                if diepiece==-1:
                    print("player %d moves %s %d -> %d"%(piecelist[movingpiece].position,piecelist[movingpiece].typ,fromspot,tospot))
                    board[fromspot]=-1
                    board[tospot]=movingpiece
                    fromspot=-1
                    piecelist[movingpiece].spot_x=spotlist[tospot][0]
                    piecelist[movingpiece].spot_y=spotlist[tospot][1]
                    if diepiece!=-1 and piecelist[movingpiece].position!=piecelist[diepiece].position:
                        if piecelist[movingpiece].position==1:
                            piecelist[diepiece].position=1
                            hand1.append(diepiece)
                        elif piecelist[movingpiece].position==2:
                            piecelist[diepiece].position=2
                            hand2.append(diepiece)
                    showboard()
                    tospot=-1
                    movingpiece=-1
                    diepiece=-1
                elif diepiece!=-1 and piecelist[movingpiece].position!=piecelist[diepiece].position:
                    print("player %d moves %s %d -> %d"%(piecelist[movingpiece].position,piecelist[movingpiece].typ,fromspot,tospot))
                    board[fromspot]=-1
                    board[tospot]=movingpiece
                    fromspot=-1
                    piecelist[movingpiece].spot_x=spotlist[tospot][0]
                    piecelist[movingpiece].spot_y=spotlist[tospot][1]
                    if diepiece!=-1 and piecelist[movingpiece].position!=piecelist[diepiece].position:
                        if piecelist[movingpiece].position==1:
                            piecelist[diepiece].position=1
                            hand1.append(diepiece)
                        elif piecelist[movingpiece].position==2:
                            piecelist[diepiece].position=2
                            hand2.append(diepiece)
                    showboard()
                    tospot=-1
                    movingpiece=-1
                    diepiece=-1
                else:
                    print('illegal move1 by ',piecelist[movingpiece].typ,fromspot,'->',tospot)
                    piecelist[movingpiece].spot_x=spotlist[fromspot][0]
                    piecelist[movingpiece].spot_y=spotlist[fromspot][1]
                    showboard()
                    fromspot=-1
                    tospot=-1
                    movingpiece=-1
                    diepiece=-1
            else:
                print('illegal move2 by ',piecelist[movingpiece].typ,fromspot,'->',tospot)
                piecelist[movingpiece].spot_x=spotlist[fromspot][0]
                piecelist[movingpiece].spot_y=spotlist[fromspot][1]
                showboard()
                fromspot=-1
                tospot=-1
                movingpiece=-1
                diepiece=-1
        if hand1toboard!=-1:
            piecelist[hand1[hand1toboard]].spot_x=pygame.mouse.get_pos()[0]-60
            piecelist[hand1[hand1toboard]].spot_y=pygame.mouse.get_pos()[1]-60
        if hand2toboard!=-1:
            piecelist[hand2[hand2toboard]].spot_x=pygame.mouse.get_pos()[0]-60
            piecelist[hand2[hand2toboard]].spot_y=pygame.mouse.get_pos()[1]-60
        if hand1board!=-1:
            piecelist[hand1[hand1toboard]].spot_x=spotlist[hand1board][0]
            piecelist[hand1[hand1toboard]].spot_y=spotlist[hand1board][1]
            piecelist[hand1[hand1toboard]].moving=0
            board[hand1board]=hand1[hand1toboard]
            del hand1[hand1toboard]
            hand1toboard=-1
            hand1board=-1
        if hand2board!=-1:
            piecelist[hand2[hand2toboard]].spot_x=spotlist[hand2board][0]
            piecelist[hand2[hand2toboard]].spot_y=spotlist[hand2board][1]
            piecelist[hand2[hand2toboard]].moving=0
            board[hand2board]=hand2[hand2toboard]
            del hand2[hand2toboard]
            hand2toboard=-1
            hand2board=-1
        gamepad.fill(WHITE)
        back(0,0)
        placepiece()
        pygame.display.update()
        clock.tick(10)
    pygame.quit()
        
def initGame():
    global gamepad, clock,background,piecelist,spotlist,board
    
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width,pad_height))
    pygame.display.set_caption('십이장기')
    clock=pygame.time.Clock()
    background = pygame.image.load("img/판.png")
    runGame()
    
initGame()


# In[2]:


print()


# In[ ]:





# In[ ]:




