import  pygame,time, math, random, sys,os,random,gpio
from pygame.locals import *

dino1 = pygame.image.load('dino1.png')
dino2 = pygame.image.load('dino2.png')
background = pygame.image.load('bg.png')
background1 = pygame.image.load('bg.png')
background2 = pygame.image.load('bg2.png')
background3 = pygame.image.load('bg3.png')
background4 = pygame.image.load('bg4.png')
background5 = pygame.image.load('bg5.png')
backgroundx = pygame.image.load('bgx.png')
e0= pygame.image.load('energy_0.png')
e1= pygame.image.load('energy_1.png')
e2= pygame.image.load('energy_2.png')
e3= pygame.image.load('energy_3.png')
e4= pygame.image.load('energy_4.png')
e5= pygame.image.load('energy_5.png')
e6= pygame.image.load('energy_6.png')
e7= pygame.image.load('energy_7.png')
e8= pygame.image.load('energy_8.png')
e9= pygame.image.load('energy_9.png')
e10= pygame.image.load('energy_10.png')
sky1 = pygame.image.load('sk1.png')
sky2 = pygame.image.load('sk2.png')
gameover = pygame.image.load('gameover.png')
sheld= pygame.image.load('sheld.png')


W, H = 600, 400
HW, HH = W / 2, H / 2
AREA = W * H
FPS = 100
bg_x = 0
sk_x = 0

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((W,H))

skset=[sky1,sky2]
bgset=[background1,background2,background3,background4,background5]
#bgset=[background1,background1,background1,background1,background1]
d = [[872,220,909],[1207,196,1248],[1655,218,1693],[2184,225,2218],[2676,189,2727],[3271,198,3317]]
d1 = [[872,220,909],[1207,196,1248],[1655,218,1693],[2184,225,2218],[2676,189,2727],[3271,198,3317]]
d2 = [[150,175,190],[414,221,595],[982,173,1021],[1411,185,1446],[1650,227,1781],[3222,175,3276]]
d3 = [[546,141,613],[1177,153,1252],[1983,109,2009],[2741,177,3005],[3781,125,3850]]
d4 = [[270,151,365],[666,178,908],[1706,226,2026],[3169,117,3301]]
dset=[d1,d2,d3,d4]
#dset=[d1,d1,d1,d1]
e=[e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]


class David():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isJump = False
        self.jumpCount = 15

    def draw(self,x,op,fly):
        myFont = pygame.font.SysFont("Times New Roman", 18)
        mytime = myFont.render(str(pygame.time.get_ticks()/1000)+'s',1,(0,0,0))
        screen.blit(mytime,(x+20,int(self.y)+20))
        if op==1:
            screen.blit(dino1, (x,int(self.y)))
        else:
            screen.blit(dino2, (x,int(self.y)))
        if fly:
            screen.blit(sheld, (x-20,int(self.y)-5)) 

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
            myFont = pygame.font.SysFont("Times New Roman", 30)
            mytime = myFont.render("Your score is : "+str(pygame.time.get_ticks()),1,(0,0,0))
            screen.blit(gameover,(0,0))
            screen.blit(mytime,(300,350))
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
            sys.exit()
    def  check_test(self,x,z,d,bg_x):#check hit position
        if ( (x>=d[z][0]) and (self.y>=d[z][1]) and (x<=d[z][2])):
            if d==d1:
                print('bg1',z)
            if d==d2:
                print('bg2',z)
            if d==d3:
                print('bg3',z)
            if d==d4:
                print('bg4',z)
            
        
            
image_width = 20  #if you change the image , you need to fill new image width       
pos_x = 50
pos_y = 259-image_width
david = David(pos_x, pos_y)
next_bg=random.randint(0,len(dset)-1)
next_sk=random.randint(0,1)
ground_speed = 5
sky_speed = 1
z=0
op = 1 # op change image of dino
energy=0
fly=0
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_SPACE:
                david.isJump = True
            if event.key == pygame.K_a:
                fly=1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                fly=0

    clock.tick(FPS)
    pressed_keys = pygame.key.get_pressed()
    screen.blit(background, (bg_x,0))
    screen.blit(bgset[next_bg], (bg_x+4000,0))
    screen.blit(sky1,(sk_x,0))
    screen.blit(skset[next_sk],(sk_x+4000,0))

    if(z<len(d)-1 and d[z][2]<pos_x-bg_x):
        z = z+1
    if fly and energy>250:
        energy=energy-5;
        
        
    else:
        david.check((pos_x-bg_x),z,d,bg_x)#change check_test if debug
        if energy<1000:
            energy=energy+1
    
    david.draw(pos_x,op,fly and energy>250)
    david.jump()
    bg_x = bg_x-ground_speed
    sk_x = sk_x-sky_speed
    if op==1: op=2 #change Dino picture for every loop 
    else: op=1
    
    if bg_x<=-4000:
        ground_speed = min(ground_speed,8)
        bg_x=bg_x+4000
        z=0
        if next_bg==0:
            background = pygame.image.load('bg.png')
        elif next_bg==1:
            background = pygame.image.load('bg2.png')
        elif next_bg==2:
            background = pygame.image.load('bg3.png')
        elif next_bg==3:
            background = pygame.image.load('bg4.png')
        elif next_bg==4:
            background = pygame.image.load('bg5.png')
        next_bg=random.randint(0,len(dset)-1)
        #next_bg=4
        d=dset[next_bg][:]
    if sk_x <= -4000:
        sky_speed= min(sky_speed+1,5)
        sk_x = sk_x+4000
        if next_sk == 0:
            sky1 = pygame.image.load('sk1.png')
        elif next_sk==1:
            sky1 = pygame.image.load('sk2.png')
        next_sk = random.randint(0,1)
    screen.blit(e[int(energy/100)],(300,300))
    pygame.display.update()
