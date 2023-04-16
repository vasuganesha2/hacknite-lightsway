import pygame
import math
import sys
pygame.init()
text_font=pygame.font.Font(None,50)
text1_font=pygame.font.Font(None,69)
text2_font=pygame.font.Font(None,100)
clock=pygame.time.Clock()
screen=pygame.display.set_mode((1721,1007))
player_style=pygame.image.load(r"./goku.jpg")
player_style=pygame.transform.rotozoom(player_style,0,1)
player_rect=player_style.get_rect(center=(860,503))
game_active=False
active=False
text1=text_font.render("GOKU THE LEGEND",False,'White')
text1_rect=text1.get_rect(center=(860,50))
text2=text_font.render("NEW GAME",False,'White')
text2_rect=text2.get_rect(center=(1610,750))
texta=text1_font.render("EASY",False,'White')
text_a=texta.get_rect(center=(860,440))
textb=text1_font.render("MEDIUM",False,'White')
text_b=texta.get_rect(center=(860,480))
textc=text1_font.render("HARD",False,'White')
text_c=texta.get_rect(center=(860,520))
message=text2_font.render("KHELO DIMAG SE",False,'White')
message_rect=message.get_rect(center=(860,150))
text_b=texta.get_rect(center=(860,480))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Set the font and size
font = pygame.font.Font(None, 36)
# Set the progress bar position and size
bar_pos = (50, 50)
bar_width = 600
bar_height = 20
# Set the progress bar color and border color
bar_color = 'RED'
border_color = BLACK
# Set the progress bar value
progress = 0.0
wallpaper=pygame.image.load(r"./wallpaper.jpg")
wallpaper_rect=pygame.transform.rotozoom(wallpaper,0,1)
goku=pygame.image.load(r"./gokkuw.png")
goku_rect=pygame.transform.rotozoom(goku,0,0.5)
goku_rect=goku_rect.get_rect(center=(806,503))
wallpaper_rect=wallpaper_rect.get_rect(center=(806,503))
game_Active=False
# Run the game loop
done = False
font = pygame.font.SysFont(None, 30)

# Set up loading spinner
spinner_width = 50
spinner_radius = spinner_width // 2
spinner_center = (50,50)
spinner_angle = 0
spinner_speed = 0.1

bullets = pygame.sprite.Group()


pygame.display.set_caption("Illuminae")
# bg = pygame.image.load('/home/tanish/Desktop/GAMES/bg.jpg')

clock=pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
all_hitboxes=[]
MAP_WIDTH = 40
MAP_HEIGHT = 23
TILE_SIZE = 42
winWidth=MAP_WIDTH*TILE_SIZE
winHeight=MAP_HEIGHT*TILE_SIZE
win=pygame.display.set_mode((winWidth+41,winHeight+41)); #((1721,1007))

MAP_DATA = [
   [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
   [5, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 5],
   [5, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 5],
   [5, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 5],
   [5, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 5],
   [5, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 4, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 4, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 4, 0, 0, 4, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 4, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 4, 4, 4, 4, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 4, 4, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 4, 0, 0, 4, 0, 4, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
]

walkLeft=[pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_left_walk.000.gif'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_left_walk.001.gif'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_left_walk.002.gif'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_left_walk.003.gif'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_left_walk.004.gif'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_left_walk.005.gif')]
walkRight=[pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_right_walk.000.xcf'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_right_walk.001.xcf'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_right_walk.002.xcf'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_right_walk.003.xcf'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_right_walk.004.xcf'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_right_walk.005.xcf')]
walkUp=[pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_back_walk.000.gif'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_back_walk.001.gif'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_back_walk.002.gif'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_back_walk.003.gif'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_back_walk.004.gif'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_back_walk.005.gif')]
walkDown=[pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_front_walk.000.gif'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_front_walk.001.gif'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_front_walk.002.gif'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_front_walk.003.gif'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_front_walk.004.gif'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_front_walk.005.gif')]
char=pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_front.gif')

wDown_e1=[pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e1b0.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e1b1.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e1b2.png')]
wLeft_e1=[pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e1l0.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e1l1.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e1l2.png')]
wRight_e1=[pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e1r0.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e1r1.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e1r2.png')]
wUp_e1=[pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e1f0.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e1f1.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e1f2.png')]

wDown_e2=[pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e2b0.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e2b1.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e2b2.png')]
wLeft_e2=[pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e2l0.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e2l1.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e2l2.png')]
wRight_e2=[pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e2r0.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e2r1.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e2r2.png')]
wUp_e2=[pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e2f0.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e2f1.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e2f2.png')]

wDown_e3=[pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e3b0.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e3b1.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e3b2.png')]
wLeft_e3=[pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e3l0.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e3l1.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e3l2.png')]
wRight_e3=[pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e3r0.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e3r1.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e3r2.png')]
wUp_e3=[pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e3f0.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e3f1.png'),pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e3f2.png')]

scale_factor = 5
walkDown_e1 = []
walkLeft_e1=[]
walkRight_e1=[]
walkUp_e1=[]

walkDown_e2 = []
walkLeft_e2=[]
walkRight_e2=[]
walkUp_e2=[]

walkDown_e3 = []
walkLeft_e3=[]
walkRight_e3=[]
walkUp_e3=[]

for image in wDown_e1:
    zoomed_image = pygame.transform.scale(image, (image.get_width() * scale_factor/2, image.get_height() * scale_factor))
    walkDown_e1.append(zoomed_image)
for image in wLeft_e1:
    zoomed_image = pygame.transform.scale(image, (image.get_width() * scale_factor/2, image.get_height() * scale_factor))
    walkLeft_e1.append(zoomed_image)
for image in wRight_e1:
    zoomed_image = pygame.transform.scale(image, (image.get_width() * scale_factor/2, image.get_height() * scale_factor))
    walkRight_e1.append(zoomed_image)
for image in wUp_e1:
    zoomed_image = pygame.transform.scale(image, (image.get_width() * scale_factor/2, image.get_height() * scale_factor))
    walkUp_e1.append(zoomed_image)
    
for image in wDown_e2:
    zoomed_image = pygame.transform.scale(image, (image.get_width() * scale_factor/2, image.get_height() * scale_factor))
    walkDown_e2.append(zoomed_image)
for image in wLeft_e2:
    zoomed_image = pygame.transform.scale(image, (image.get_width() * scale_factor/2, image.get_height() * scale_factor))
    walkLeft_e2.append(zoomed_image)
for image in wRight_e2:
    zoomed_image = pygame.transform.scale(image, (image.get_width() * scale_factor/2, image.get_height() * scale_factor))
    walkRight_e2.append(zoomed_image)
for image in wUp_e2:
    zoomed_image = pygame.transform.scale(image, (image.get_width() * scale_factor/2, image.get_height() * scale_factor))
    walkUp_e2.append(zoomed_image)
    
for image in wDown_e3:
    zoomed_image = pygame.transform.scale(image, (image.get_width() * scale_factor/2, image.get_height() * scale_factor))
    walkDown_e3.append(zoomed_image)
for image in wLeft_e3:
    zoomed_image = pygame.transform.scale(image, (image.get_width() * scale_factor/2, image.get_height() * scale_factor))
    walkLeft_e3.append(zoomed_image)
for image in wRight_e3:
    zoomed_image = pygame.transform.scale(image, (image.get_width() * scale_factor/2, image.get_height() * scale_factor))
    walkRight_e3.append(zoomed_image)
for image in wUp_e3:
    zoomed_image = pygame.transform.scale(image, (image.get_width() * scale_factor/2, image.get_height() * scale_factor))
    walkUp_e3.append(zoomed_image)


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 8
        self.left = False
        self.right = False
        self.up=False
        self.down=False
        self.standing=True
        self.walkCount = 0
        self.last_direction=""
        self.hitbox=(self.x,self.y,35,65)        
        self.hitbox_d1=(self.x,self.y,150,150)        
        self.hitbox_d2=((self.x+self.width//2-50),(self.y+self.height//2-50),100,100)  
        self.has_key1=False
        self.has_key2=False
        self.has_key3=False      
        
    def draw(self, win):
        if self.walkCount + 1 >= 18:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
            self.last_direction = "left"
            self.standing=False
        elif self.right:
            win.blit(walkRight[self.walkCount//3],(self.x,self.y))
            self.walkCount +=1
            self.last_direction = "right"
            self.standing=False
        elif self.up:
            win.blit(walkUp[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
            self.last_direction = "up"
            self.standing=False
        elif self.down:
            win.blit(walkDown[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
            self.last_direction = "down"
            self.standing=False
        else:
            event=pygame.event.get()
            if len(event)==0:   
                self.standing=True
            if self.standing==True:
                win.blit(pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_front.gif'),(self.x,self.y))
            if self.last_direction == "left":
                win.blit(pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_left.gif'),(self.x,self.y))
            elif self.last_direction == "right":
                win.blit(pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_right.xcf'),(self.x,self.y))
            elif self.last_direction == "up":
                win.blit(pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_back.gif'),(self.x,self.y))
            elif self.last_direction == "down":
                win.blit(pygame.image.load('/home/tanish/Desktop/GAMES/sprites/crono_front.gif'),(self.x,self.y))
                
        self.hitbox_d1=((self.x+self.width//2-50),(self.y+self.height//2-50),100,100)
        self.hitbox_d2=((self.x+self.width//2-200),(self.y+self.height//2-200),400,400)
        self.hitbox_c1=((self.x+self.width//2-50),(self.y+self.height//2-50),100,100)               
        pygame.draw.rect(win,(255,0,0),(self.hitbox_d1),2)
        pygame.draw.rect(win,(255,0,0),(self.hitbox_d2),2)
        pygame.draw.circle(win,(255,0,0),(man.hitbox_c1[0]+50,man.hitbox_c1[1]+47),71,2)
    
class Projectile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, direction):
        super().__init__()
        self.x=x
        self.y=y
        self.direction=direction
        if direction == "left":
            self.image = pygame.image.load("/home/tanish/Desktop/GAMES/sprites/bullet_left.xcf")
        elif direction == "right":
            self.image = pygame.image.load("/home/tanish/Desktop/GAMES/sprites/bullet_right.xcf")
        elif direction == "up":
            self.image = pygame.image.load("/home/tanish/Desktop/GAMES/sprites/bullet_up.png")
        elif direction == "down":
            self.image = pygame.image.load("/home/tanish/Desktop/GAMES/sprites/bullet_down.xcf")
        
        self.rect = self.image.get_rect()
        self.rect.x=x 
        self.rect.y=y
        
        
    def update(self):
        if self.direction == "left":
            self.rect.x -= 5
            self.hitbox=pygame.Rect(self.rect.x,self.rect.y,50,20)
        elif self.direction == "right":
            self.rect.x += 5
            self.hitbox=pygame.Rect(self.rect.x,self.rect.y,50,20)
        elif self.direction == "up":
            self.rect.y -= 5
            self.hitbox=pygame.Rect(self.rect.x,self.rect.y,20,50)
        elif self.direction == "down":
            self.rect.y += 5
            self.hitbox=pygame.Rect(self.rect.x,self.rect.y,20,50)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        if detect_collision(self.hitbox,HITBOXES):
            self.kill()
    
 
        
        
        

                
class enemy1(object):
    def __init__(self,x,y,width,height,end_h,end_v):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.vel=4.1
        self.end_h=end_h
        self.end_v=end_v
        self.path_h=[self.x,self.end_h]
        self.path_v=[self.x,self.end_v]
        self.left=False
        self.right=False
        self.up=False
        self.down=False
        self.standing=False
        self.last_direction=""
        self.walkCount=0
        self.x_phase=True
        self.hitbox_1=(self.x,self.y,35,70)
        self.hitbox_2=(self.x,self.y,40,100)        
        
    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft_e1[self.walkCount//3],(self.x,self.y))
            self.last_direction = "left"
            self.walkCount += 1
            self.standing=False
        elif self.right:
            win.blit(walkRight_e1[self.walkCount//3],(self.x,self.y))
            self.last_direction = "right"
            self.walkCount += 1
            self.standing=False
        elif self.up:
            win.blit(walkUp_e1[self.walkCount//3],(self.x,self.y))
            self.last_direction = "up"
            self.walkCount += 1
            self.standing=False
        elif self.down:
            win.blit(walkDown_e1[self.walkCount//3],(self.x,self.y))
            self.last_direction = "down"
            self.walkCount += 1
            self.standing=False
        else:
            if self.last_direction == "left":
                win.blit(pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e1l0.png'),(self.x,self.y))
            elif self.last_direction == "right":
                win.blit(pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e1r0.png'),(self.x,self.y))
            elif self.last_direction == "up":
                win.blit(pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e1b0.png'),(self.x,self.y))
            elif self.last_direction == "down":
                win.blit(pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e1f0.png'),(self.x,self.y))
            win.blit(walkUp_e1[0], (self.x,self.y))
        self.hitbox_1=(self.x,self.y,35,70)
        self.hitbox_2=(self.x-40,self.y-30,120,120)      
        pygame.draw.rect(win,(255,0,0),enemy_1.hitbox_1,2)
        pygame.draw.rect(win,(255,0,0),enemy_1.hitbox_2,2)

    def move(self):
        if self.vel > 0:
            if self.walkCount < 3:
                if self.x + self.vel < self.path_h[1]:
                    self.x += self.vel
                else:
                    self.vel *= -1
                    self.walkCount += 1
            elif self.walkCount < 18:
                if self.y + self.vel < self.path_v[1]:
                    self.y += self.vel
                else:
                    self.vel *= -1
                    self.walkCount += 1
            else:
                self.walkCount = 0
        else:
            if self.walkCount < 3:
                if self.x - self.vel > self.path_h[0]:
                    self.x += self.vel
                else:
                    self.vel *= -1
                    self.walkCount += 1
            elif self.walkCount < 18:
                if self.y - self.vel > self.path_v[0]:
                    self.y += self.vel
                else:
                    self.vel *= -1
                    self.walkCount += 1
            else:
                self.walkCount = 0
                
class enemy2(object):
    def __init__(self,x,y,width,height,end_h,end_v):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.vel=4.1
        self.end_h=end_h
        self.end_v=end_v
        self.path_h=[self.x,self.end_h]
        self.path_v=[self.x,self.end_v]
        self.left=False
        self.right=False
        self.up=False
        self.down=False
        self.standing=False
        self.last_direction=""
        self.walkCount=0
        self.x_phase=True
        self.hitbox_1=(self.x,self.y,35,70)
        self.hitbox_2=(self.x,self.y,40,100)        
        
    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft_e2[self.walkCount//3],(self.x,self.y))
            self.last_direction = "left"
            self.walkCount += 1
            self.standing=False
        elif self.right:
            win.blit(walkRight_e2[self.walkCount//3],(self.x,self.y))
            self.last_direction = "right"
            self.walkCount += 1
            self.standing=False
        elif self.up:
            win.blit(walkUp_e2[self.walkCount//3],(self.x,self.y))
            self.last_direction = "up"
            self.walkCount += 1
            self.standing=False
        elif self.down:
            win.blit(walkDown_e2[self.walkCount//3],(self.x,self.y))
            self.last_direction = "down"
            self.walkCount += 1
            self.standing=False
        else:
            if self.last_direction == "left":
                win.blit(pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e2l0.png'),(self.x,self.y))
            elif self.last_direction == "right":
                win.blit(pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e2r0.png'),(self.x,self.y))
            elif self.last_direction == "up":
                win.blit(pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e2b0.png'),(self.x,self.y))
            elif self.last_direction == "down":
                win.blit(pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e2f0.png'),(self.x,self.y))
            win.blit(walkUp_e2[0], (self.x,self.y))
        self.hitbox_1=(self.x,self.y,35,70)
        self.hitbox_2=(self.x-40,self.y-30,120,120)      
        pygame.draw.rect(win,(255,0,0),enemy_2.hitbox_1,2)
        pygame.draw.rect(win,(255,0,0),enemy_2.hitbox_2,2)

    def move(self):
        if self.vel > 0:
            if self.walkCount < 3:
                if self.x + self.vel < self.path_h[1]:
                    self.x += self.vel
                else:
                    self.vel *= -1
                    self.walkCount += 1
            elif self.walkCount < 18:
                if self.y + self.vel < self.path_v[1]:
                    self.y += self.vel
                else:
                    self.vel *= -1
                    self.walkCount += 1
            else:
                self.walkCount = 0
        else:
            if self.walkCount < 3:
                if self.x - self.vel > self.path_h[0]:
                    self.x += self.vel
                else:
                    self.vel *= -1
                    self.walkCount += 1
            elif self.walkCount < 18:
                if self.y - self.vel > self.path_v[0]:
                    self.y += self.vel
                else:
                    self.vel *= -1
                    self.walkCount += 1
            else:
                self.walkCount = 0

class enemy3(object):
    def __init__(self,x,y,width,height,end_h,end_v):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.vel=4.1
        self.end_h=end_h
        self.end_v=end_v
        self.path_h=[self.x,self.end_h]
        self.path_v=[self.x,self.end_v]
        self.left=False
        self.right=False
        self.up=False
        self.down=False
        self.standing=False
        self.last_direction=""
        self.walkCount=0
        self.x_phase=True
        self.hitbox_1=(self.x,self.y,35,70)
        self.hitbox_2=(self.x,self.y,40,100)        
        
    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft_e3[self.walkCount//3],(self.x,self.y))
            self.last_direction = "left"
            self.walkCount += 1
            self.standing=False
        elif self.right:
            win.blit(walkRight_e3[self.walkCount//3],(self.x,self.y))
            self.last_direction = "right"
            self.walkCount += 1
            self.standing=False
        elif self.up:
            win.blit(walkUp_e3[self.walkCount//3],(self.x,self.y))
            self.last_direction = "up"
            self.walkCount += 1
            self.standing=False
        elif self.down:
            win.blit(walkDown_e3[self.walkCount//3],(self.x,self.y))
            self.last_direction = "down"
            self.walkCount += 1
            self.standing=False
        else:
            if self.last_direction == "left":
                win.blit(pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e3l0.png'),(self.x,self.y))
            elif self.last_direction == "right":
                win.blit(pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e3r0.png'),(self.x,self.y))
            elif self.last_direction == "up":
                win.blit(pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e3b0.png'),(self.x,self.y))
            elif self.last_direction == "down":
                win.blit(pygame.image.load('/home/tanish/Desktop/GAMES/sprites/enemy/e3f0.png'),(self.x,self.y))
            win.blit(walkUp_e3[0], (self.x,self.y))
        self.hitbox_1=(self.x,self.y,35,70)
        self.hitbox_2=(self.x-40,self.y-30,120,120)      
        pygame.draw.rect(win,(255,0,0),enemy_3.hitbox_1,2)
        pygame.draw.rect(win,(255,0,0),enemy_3.hitbox_2,2) 

    def move(self):
        if self.vel > 0:
            if self.walkCount < 3:
                if self.x + self.vel < self.path_h[1]:
                    self.x += self.vel
                else:
                    self.vel *= -1
                    self.walkCount += 1
            elif self.walkCount < 18:
                if self.y + self.vel < self.path_v[1]:
                    self.y += self.vel
                else:
                    self.vel *= -1
                    self.walkCount += 1
            else:
                self.walkCount = 0
        else:
            if self.walkCount < 3:
                if self.x - self.vel > self.path_h[0]:
                    self.x += self.vel
                else:
                    self.vel *= -1
                    self.walkCount += 1
            elif self.walkCount < 18:
                if self.y - self.vel > self.path_v[0]:
                    self.y += self.vel
                else:
                    self.vel *= -1
                    self.walkCount += 1
            else:
                self.walkCount = 0








    
def draw_map():
    for row in range(MAP_HEIGHT):
        for col in range(MAP_WIDTH):
            tile_type = MAP_DATA[row][col]
            tile_color = None
            if tile_type == 5:
                tile_color = (0,255,0)
            elif tile_type == 4:
                tile_color = (0,0,255) 
            elif tile_type == 1:
                tile_color = (255,255,255)
            elif tile_type == 0:
                tile_color = (0,0,0)
     
# def redrawGameWindow():   
#     win.blit((0,0,0))
#     man.draw(win)
#     enemy_1.draw(win)
#     for bullet in bullets:
#         bullet.draw(win)
    
#     if bullet.hitbox.colliderect(man.hitbox_d2):
#         bullets.remove(bullet)
#     pygame.display.update()
#     pygame.draw.rect(win,(255,0,0),man.hitbox,2)
    
#     #pygame.display.update()
#     HITBOXES=create_hitboxes(MAP_DATA, 42, 42)
#     for hitbox in HITBOXES:
#         pygame.draw.rect(win, (255, 0, 0), hitbox, 1)

def redrawGameWindow():   
    win.fill((0,0,0)) # fill the window with black color
    man.draw(win)
    enemy_1.draw(win)
    enemy_2.draw(win)
    enemy_3.draw(win)
    bullets.draw(win)
    # if bullet.hitbox.colliderect(man.hitbox_d2):
    #     bullet.kill()

    pygame.draw.rect(win,(255,0,0),man.hitbox,2)
    pygame.draw.rect(win,(255,0,0),enemy_1.hitbox_1,2)
    #pygame.display.update()
    HITBOXES=create_hitboxes(MAP_DATA, 42, 42)
    for hitbox in HITBOXES:
        pygame.draw.rect(win, (255, 0, 0), hitbox, 1)
    # pygame.display.update()
def update_map_data(map_data,character):
    if character.has_key:
        for row in map_data:
            if 3 in row:
                row[row.index(3)] = 0
    return map_data

def create_hitbox(length, width, x, y):
    hitbox = pygame.Rect(x, y, length, width)
    return hitbox


# def create_hitboxes(map_data, hitbox_length, hitbox_width):
#     global all_hitboxes
#     temp_surface = pygame.Surface(win.get_size(), pygame.SRCALPHA)
#     hitbox_x = 0
#     hitbox_y = 0
#     temp_surface.fill((0, 0, 0, 0))
#     for i in range(len(map_data)):
#         for j in range(len(map_data[i])):
#             if map_data[i][j] == 4:
#                 hitbox = create_hitbox(hitbox_length, hitbox_width, hitbox_x, hitbox_y)
#                 all_hitboxes.append(hitbox)
#                 pygame.draw.rect(win, (255, 0, 0), hitbox, 1)
#             elif map_data[i][j] == 5:
#                 hitbox = create_hitbox(hitbox_length, hitbox_width, hitbox_x, hitbox_y)
#                 all_hitboxes.append(hitbox)
#                 pygame.draw.rect(win, (255, 255, 0), hitbox, 1)
#                 if man.hitbox.colliderect(hitbox):
#                     man.has_key1 = True
#             elif map_data[i][j] == 3:
#                 hitbox = create_hitbox(hitbox_length, hitbox_width, hitbox_x, hitbox_y)
#                 all_hitboxes.append(hitbox)
#                 pygame.draw.rect(win, (255, 255, 0), hitbox, 1)
#                 if man.hitbox.colliderect(hitbox):
#                     map_data[i][j] = 0
#                     man.has_key1=True
#                 all_hitboxes.remove(hitbox)
#             hitbox_x += hitbox_length
#         hitbox_x = 0
#         hitbox_y += hitbox_width
#     win.blit(temp_surface, (0, 0))
#     pygame.display.flip()
#     return all_hitboxes

def create_hitboxes(map_data, hitbox_length, hitbox_width):
    global all_hitboxes
    temp_surface = pygame.Surface(win.get_size(), pygame.SRCALPHA)
    hitbox_x = 0
    hitbox_y = 0
    temp_surface.fill((0, 0, 0, 0))
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if map_data[i][j] == 0:
                image = pygame.image.load(r"./tiles1.jpg")
                image = pygame.transform.scale(image, (hitbox_length, hitbox_width))
                image_rect = image.get_rect(center=(hitbox_x, hitbox_y))
                win.blit(image, image_rect)
            if map_data[i][j] == 4:
                hitbox = create_hitbox(hitbox_length, hitbox_width, hitbox_x, hitbox_y)
                all_hitboxes.append(hitbox)
                image = pygame.image.load(r"./tiles2.jpg")
                image = pygame.transform.scale(image, (hitbox_length, hitbox_width))
                image_rect = image.get_rect(center=(hitbox_x, hitbox_y))
                win.blit(image, image_rect)
            elif map_data[i][j] == 5:
                hitbox = create_hitbox(hitbox_length, hitbox_width, hitbox_x, hitbox_y)
                all_hitboxes.append(hitbox)
                pygame.draw.rect(win, (255, 255, 0), hitbox, 1)
                if man.hitbox.colliderect(hitbox):
                    man.has_key1 = True
                if man.hitbox.colliderect(hitbox):
                    man.has_key1 = True
            elif map_data[i][j] == 3:
                hitbox = create_hitbox(hitbox_length, hitbox_width, hitbox_x, hitbox_y)
                all_hitboxes.append(hitbox)
                pygame.draw.rect(win, (255, 255, 0), hitbox, 1)
                if man.hitbox.colliderect(hitbox):
                    map_data[i][j] = 0
                    man.has_key1 = True
                all_hitboxes.remove(hitbox)
            hitbox_x += hitbox_length
        hitbox_x = 0
        hitbox_y += hitbox_width
    win.blit(temp_surface, (0, 0))
    pygame.display.flip()
    return all_hitboxes

def detect_collision(character_rect, hitboxes):
    for hitbox in hitboxes:
        if character_rect.colliderect(hitbox):
            return True
    return False

def handle_collision(character_rect, hitboxes):
    for hitbox in hitboxes:
        if character_rect.colliderect(hitbox):
            if character_rect.left < hitbox.left:
                character_rect.right = hitbox.left
            elif character_rect.right > hitbox.right:
                character_rect.left = hitbox.right
            elif character_rect.top < hitbox.top:
                character_rect.bottom = hitbox.top
            elif character_rect.bottom > hitbox.bottom:
                character_rect.top = hitbox.bottom
    return(character_rect)            
            
man = player(90,82,39,75)
enemy_1=enemy1(200,280,39,75,255,245)
enemy_2=enemy2(280,240,39,75,280,300)
enemy_3=enemy3(400,300,39,75,450,300)
run = True
shootloop=0
draw_map()
active_bullets = pygame.sprite.Group()
MAX_BULLETS = 1
bullet_sprites = pygame.sprite.Group()
easy=False
medium=False
Hard=False
while True:
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            pygame.quit()
            exit()
        if(event.type==pygame.MOUSEBUTTONDOWN and text2_rect.collidepoint(pygame.mouse.get_pos())):
            active=True
        if(event.type==pygame.MOUSEBUTTONDOWN and text_a.collidepoint(pygame.mouse.get_pos())):
            done=True
            easy=True
        if(event.type==pygame.MOUSEBUTTONDOWN and text_a.collidepoint(pygame.mouse.get_pos())):
            done=True
            medium=True
        if(event.type==pygame.MOUSEBUTTONDOWN and text_a.collidepoint(pygame.mouse.get_pos())):
            done=True
            hard=True
    screen.fill("black")
    #pygame.draw.ellipse(screen,'blue',pygame.Rect(615,350,500,300))
    screen.blit(text1,text1_rect)
    screen.blit(player_style,player_rect)
    pygame.draw.ellipse(screen,'blue',pygame.Rect(1500,700,215,100))
    screen.blit(text2,text2_rect)
    if(active):
        screen.blit(wallpaper,wallpaper_rect)
        screen.blit(goku,goku_rect)
        if progress < 2.0:
           progress += 0.01
        else:
            game_active=True
            active=False
        spinner_outline = pygame.Rect(spinner_center[0] - spinner_radius, spinner_center[1] - spinner_radius, spinner_width, spinner_width)
        pygame.draw.arc(screen, 'GREY', spinner_outline, 0, math.pi * 2, 3)
        spinner_angle += spinner_speed
        spinner_pivot = (spinner_center[0] + spinner_radius * math.cos(spinner_angle), spinner_center[1] + spinner_radius * math.sin(spinner_angle))
        pygame.draw.line(screen, 'blue', spinner_center, spinner_pivot, 3)
    
    # Draw the loading text
        loading_text = "Loading"
        loading_text += "." * ((pygame.time.get_ticks() // 500) % 4)
        loading_surface = font.render(loading_text, True, 'white')
        loading_rect = loading_surface.get_rect(center=(50, 100))
        screen.blit(loading_surface, loading_rect)
           #pygame.draw.rect(screen, border_color, [bar_pos[0], bar_pos[1], bar_width, bar_height], 2)
    # Draw the progress bar
        #pygame.draw.rect(screen, bar_color, [bar_pos[0]+50, bar_pos[1]+350, bar_width * progress, bar_height*8])
        #screen.blit(text1,text1_rect)
    # Draw the progress percentage
        #progress_text = font.render("{:.0%}".format(progress), True, BLACK)
        #screen.blit(progress_text, (bar_pos[0] + bar_width / 2 - progress_text.get_width() / 2, bar_pos[1] + bar_height + 850))
    if(game_active and active==False):
        while run:
           for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]  and man.x > man.vel + 40:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.down=False
            man.up=False
            man.standing=False
        elif keys[pygame.K_RIGHT]  and man.x < 1645 - man.width - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False
            man.down=False
            man.up=False
            man.standing=False
        elif keys[pygame.K_UP] and man.y > man.vel + 41:
            man.y -= man.vel
            man.up=True
            man.right = False
            man.left = False
            man.down=False
            man.standing=False
        elif keys[pygame.K_DOWN] and man.y <  winHeight - man.height - man.vel:
            man.y += man.vel
            man.down=True
            man.right = False
            man.left = False
            man.up=False
            man.standing=False
        elif keys[pygame.K_SPACE] and len(active_bullets)<MAX_BULLETS:
            if man.last_direction=="left":
                bullet = Projectile("/home/tanish/Desktop/GAMES/sprites/bullet_left.xcf", man.x, man.y, "left")
            elif man.last_direction=="right":
                bullet = Projectile("/home/tanish/Desktop/GAMES/sprites/bullet_right.xcf", man.x, man.y, "right")
            elif man.last_direction=="up": 
                bullet = Projectile("/home/tanish/Desktop/GAMES/sprites/bullet_up.png", man.x, man.y, "up")
            elif man.last_direction=="down":
                bullet = Projectile("/home/tanish/Desktop/GAMES/sprites/bullet_down.xcf", man.x, man.y, "down")
            
            bullet_sprites.add(bullet)
            
            active_bullets.add(bullet)
            bullet_fired = True    
            
        active_bullets.update()     
        bullet_sprites.update()
        bullet_sprites.draw(win)

        if not(keys[pygame.K_RIGHT] or keys[pygame.K_DOWN] or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_UP]):
            man.right = False
            man.left = False
            man.down=False
            man.up=False
            man.standing=True
            man.walkCount = 0
        man.hitbox = pygame.Rect(man.x, man.y, man.width, man.height)
        enemy_1.hitbox_1=pygame.Rect(enemy_1.x,enemy_1.y,enemy_1.width,enemy_1.height)
        # man.hitbox_d1=pygame.Rect(man.x,man.y,)
        
        HITBOXES=create_hitboxes(MAP_DATA, 42, 42)
        if detect_collision(man.hitbox, HITBOXES): 
            man.hitbox = handle_collision(man.hitbox,HITBOXES)
            man.x = man.hitbox[0]
            man.y = man.hitbox[1]
        if detect_collision(enemy_1.hitbox_1,HITBOXES):
            enemy_1.hitbox_1 = handle_collision(enemy_1.hitbox_1,HITBOXES)
            enemy_1.x=enemy_1.hitbox_1[0]
            enemy_1.y=enemy_1.hitbox_1[1]
            
        win.fill((0,0,0))
        redrawGameWindow()
        pygame.display.update()
        clock.tick(60)