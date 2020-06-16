import  pygame,time, math, random, sys,os,random
from pygame.locals import *
from gpiozero import Button

def  game_initialization():
    
    global dino1,dino2,background,background1,background2,background3,background4,background5,backgroundx
    global e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10
    global sky1,sky2
    global gameover,shield
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
    shield= pygame.image.load('shield.png')

    global jump_music,die_music,shield_music
    pygame.mixer.init()
    pygame.time.delay(1000)
    jump_music = pygame.mixer.Sound('jump.wav')
    jump_music.set_volume(0.2)
    die_music = pygame.mixer.Sound('die.wav')
    die_music.set_volume(1.0)
    shield_music = pygame.mixer.Sound('shield.wav')
    shield_music .set_volume(1.0)

    pygame.mixer.music.load("david_bgm.mp3") #load bgm 
    pygame.mixer.music.play(-1)

    global FPS, bg_x, sk_x
    W, H = 600, 400
    HW, HH = W / 2, H / 2
    AREA = W * H
    FPS = 100
    bg_x = 0
    sk_x = 0

    global screen
    pygame.init()
    screen = pygame.display.set_mode((W,H))

    global skset,bgset,d,d1,d2,d3,d4,dset,e
    skset=[sky1,sky2]
    bgset=[background1,background2,background3,background4,background5]
    d = [[872,220,909],[1207,196,1248],[1655,218,1693],[2184,225,2218],[2676,189,2727],[3271,198,3317]]
    d1 = [[872,220,909],[1207,196,1248],[1655,218,1693],[2184,225,2218],[2676,189,2727],[3271,198,3317]]
    d2 = [[150,175,190],[414,221,595],[982,173,1021],[1411,185,1446],[1650,227,1781],[3222,175,3276]]
    d3 = [[546,141,613],[1177,153,1252],[1983,109,2009],[2741,177,3005],[3781,125,3850]]
    d4 = [[270,151,365],[666,178,908],[1706,226,2026],[3169,117,3301]]
    dset=[d1,d2,d3,d4]
    e=[e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]

    global clock, image, pos_x, pos_y, david, next_bg, next_sk, ground_speed, sky_speed,  flash_freq, z, op, energy,fly, flash_time, is_flash, frame, playing
    clock = pygame.time.Clock()
    image_width = 20  #if you change the image , you need to fill new image width       
    pos_x = 50
    pos_y = 259-image_width
    david = David(pos_x, pos_y)
    next_bg=random.randint(0,len(dset)-1)
    next_sk=random.randint(0,1)
    ground_speed = 5
    sky_speed = 1
    flash_freq = FPS/2
    z = 0
    op = 1 # op change image of dino
    energy = 0
    fly = 0
    flash_time = 0
    is_flash = 0
    frame = 0
    playing = 1 # playing = 1 ->  enter or replay


        
class David():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isJump = False
        self.jumpCount = 15
        

    def draw(self,x,op,fly, energy ,is_flash,frame,flash_freq):
        myFont = pygame.font.SysFont("Times New Roman", 18)
        mytime = myFont.render(str(pygame.time.get_ticks()/1000)+'s',1,(0,0,0))
        screen.blit(mytime,(x+20,int(self.y)+20))
        if op==1:
            screen.blit(dino1, (x,int(self.y)))
        else:
            screen.blit(dino2, (x,int(self.y)))
        if fly:
            screen.blit(shield, (x-20,int(self.y)-5))
        else:
            if is_flash:
                if frame < flash_freq/2:
                    screen.blit(shield, (x-20,int(self.y)-5))
 
            

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
            die_music.play()
            myFont = pygame.font.SysFont("Times New Roman", 30)
            mytime = myFont.render("Your score is : "+str(pygame.time.get_ticks()),1,(0,0,0))
            screen.blit(gameover,(0,0))
            screen.blit(mytime,(300,350))
            pygame.mixer.music.stop( ); # end the original bgm before showing the lose screen
            pygame.display.update( )#update the screen of result
            pygame.mixer.music.load('lose_bgm.mp3')# load the lose bgm
            pygame.mixer.music.play( )#play lose bgm (sad violin)
            time.sleep(11)#wait for palying whole song
            return 0
            #pygame.quit()
            #sys.exit()
        else:
            return 1
        
''' #This is teacher's reference code
def RCtime(RCpin): 
    reading = 0
    GPIO.setup(RCpin,GPIO.OUT)
    GPIO.output(RCpin,GPIO.LOW)
    time.sleep(1/FPS)
    GPIO.setup(RCpin,GPIO.IN)
    while(GPIO.input(RCpin)==GPIO.LOW):
        reading += 1
    return reading'''


def game_loop():
    
    global dino1,dino2,background,background1,background2,background3,background4,background5,backgroundx
    global e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10
    global sky1,sky2
    global gameover,shield
    global jump_music,die_music,shield_music
    global FPS, bg_x, sk_x
    global screen
    global skset,bgset,d,d1,d2,d3,d4,dset,e
    global clock, image, pos_x, pos_y, david, next_bg, next_sk, ground_speed, sky_speed,  flash_freq, z, op, energy,fly, flash_time, is_flash, frame, playing
    global threshold

    button_jump = Button(16)
    button_shield = Button(18)

    button_jump.wait_for_press() #get start signal to start game
    button_shield.wait_for_press()#same as above
    
    while True:
        
        frame=(frame+1)%flash_freq
        if button_jump.is_pressed:#this is jump
            if not david.isJump:
                        jump_music.play()
                        david.isJump = True
        if button_shield.is_pressed:#this is shield
            if fly==0:
                if energy>300 and (not is_flash):
                    shield_music.play()
                    fly = 1
                    flash_time = energy
                    ground_speed = ground_speed + 10
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                #if event.key == pygame.K_SPACE:
                    #if not david.isJump:
                        #jump_music.play()
                        #david.isJump = True
                        
                        
                #if event.key == pygame.K_a:
                    #if fly==0:
                        #if energy>300 and (not is_flash):
                            #shield_music.play()
                            #fly = 1
                            #flash_time = energy
                            #ground_speed = ground_speed + 10
            

        clock.tick(FPS)
        pressed_keys = pygame.key.get_pressed()
        screen.blit(background, (bg_x,0))
        screen.blit(bgset[next_bg], (bg_x+4000,0))
        screen.blit(sky1,(sk_x,0))
        screen.blit(skset[next_sk],(sk_x+4000,0))

        
        
        if(z<len(d)-1 and d[z][2]<pos_x-bg_x):
            z = z+1

        if not fly and not is_flash:
            playing = david.check((pos_x-bg_x),z,d,bg_x)
            if playing == 0:         # break out the game and ask for playing again or not
                break
            if energy<1000:
                energy=energy+1
                
        if fly:
            if energy>0:
                energy=max(energy-5,0)
                
            else:
                fly=0
                ground_speed = ground_speed-10
                is_flash = 1

        if is_flash:
            if flash_time>0:
                flash_time = flash_time-5
            else:
                is_flash = 0
        
        david.draw(pos_x,op,fly,energy,is_flash,frame,flash_freq)
        david.jump()
        bg_x = bg_x-ground_speed
        sk_x = sk_x-sky_speed
        
        if op==1: op=2 #change Dino picture for every loop 
        else: op=1
        
        if bg_x<=-4000:
            if not fly:
                ground_speed = min(ground_speed+1,10)
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
            d=dset[next_bg][:]
            next_bg=random.randint(0,len(dset)-1)
            
            
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

def play_again():
    print('press space  and a to play again')
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if button_jump.is_pressed:
            return 1
        else:
            return 0
                
        
def game_play():
    while True:
        game_initialization()
        game_loop()
        if not play_again():
            pygame.quit()
            sys.exit()
            break

if __name__ == '__main__':
    game_play()
            
