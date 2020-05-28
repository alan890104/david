import pygame, time, math, random, sys,os,random
from pygame.locals import *

dick = pygame.image.load('image.png')
background = pygame.image.load('bg.png')
background1 = pygame.image.load('bg.png')
background2 = pygame.image.load('bg2.png')
background3 = pygame.image.load('bg3.png')
background4 = pygame.image.load('bg4.png')
background5 = pygame.image.load('bg5.png')
gameover = pygame.image.load('gameover.png')
#background = pygame.Surface((10,10))
#background.fill((255,255,255))
#pygame.draw.rect(255,0,0), (300 40, 40))

W, H = 600, 400
HW, HH = W / 2, H / 2
AREA = W * H
FPS = 80
bg_x = 0

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((W,H))

bgset=[background1,background2,background3,background4,background5]
d = [[872,220,909],[1207,196,1248],[1655,218,1693],[2184,225,2218],[2676,189,2727],[3271,198,3317]]
dset=[d,d,d,d,d]
class David():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isJump = False
        self.jumpCount = 15

    def draw(self,x):
        screen.blit(dick, (x,self.y))


    def jump(self):
        if self.isJump:
            if self.jumpCount >= -15: 
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= self.jumpCount**2 * 0.1 * neg
                self.jumpCount -= 0.5
            else:
                self.isJump = False
                self.jumpCount = 15
     
    def check(self,x,z,d,bg_x):
        if ( (x>=d[z][0]) and (self.y>=d[z][1]) and (x<=d[z][2])):
            screen.blit(gameover,(0,0))
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
            sys.exit()
            
        
pos_x = 50
pos_y = 250
david = David(pos_x, pos_y)
next_bg=random.randint(0,4)

z=0
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_SPACE:
                david.isJump = True

    clock.tick(FPS)
    pressed_keys = pygame.key.get_pressed()
    screen.blit(background, (bg_x,0))
    screen.blit(bgset[next_bg], (bg_x+4000,0))
    

    if(z<5 and d[z][2]<pos_x-bg_x):
        z = z+1
    
    david.check((pos_x-bg_x),z,d,bg_x)
    
    david.draw(pos_x)
    david.jump()
    bg_x = bg_x-5
    if bg_x==-4000: 
        bg_x=0
        z=0
        if next_bg==1:
            background = pygame.image.load('bg.png')
        elif next_bg==2:
            background = pygame.image.load('bg2.png')
        elif next_bg==3:
            background = pygame.image.load('bg3.png')
        elif next_bg==4:
            background = pygame.image.load('bg4.png')
        elif next_bg==5:
            background = pygame.image.load('bg5.png')
        next_bg=random.randint(0,4)
        d=dset[next_bg][:]
        
            
    pygame.display.update()
