import pygame
from pygame.locals import *
import pytmx
import numpy as np
import sys
import math
pygame.init()

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
   [5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 4, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, 5],
   [5, 0, 4, 0, 0, 0, 0, 4, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, 5],
   [5, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, 5],
   [5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
   [5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
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

scale_factor = 5
walkDown_e1 = []
walkLeft_e1=[]
walkRight_e1=[]
walkUp_e1=[]
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
        self.hitbox_d1=(self.x,self.y,35,65)
        self.hitbox_d2=((self.x+self.width//2-200),(self.y+self.height//2-200),400,400)
        pygame.draw.rect(win,(255,0,0),(self.hitbox_d2),2)
    
class Projectile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, direction):
        super().__init__()
        self.x=x
        self.y=y
        if direction == "left":
            self.image = pygame.image.load("/home/tanish/Desktop/GAMES/sprites/bullet_left.xcf").convert_alpha()
        elif direction == "right":
            self.image = pygame.image.load("/home/tanish/Desktop/GAMES/sprites/bullet_right.xcf").convert_alpha()
        elif direction == "up":
            self.image = pygame.image.load("/home/tanish/Desktop/GAMES/sprites/bullet_up.png").convert_alpha()
        elif direction == "down":
            self.image = pygame.image.load("/home/tanish/Desktop/GAMES/sprites/bullet_down.xcf").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction=direction
        
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
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.vel=4.1
        self.left=False
        self.right=False
        self.up=False
        self.down=False
        self.walkCount=0
        self.hitbox_1 = pygame.Rect(self.x, self.y, 35, 70)
        self.hitbox_2 = pygame.Rect(self.x, self.y, 40, 100)       
        
    def draw(self, win):
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft_e1[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight_e1[self.walkCount//3],(self.x,self.y))
            self.walkCount +=1
        elif self.up:
            win.blit(walkUp_e1[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
        elif self.down:
            win.blit(walkDown_e1[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(walkUp_e1[0], (self.x,self.y))
        self.hitbox_1=(self.x,self.y,35,70)        
        pygame.draw.rect(win,(255,0,0),enemy_1.hitbox_1,2)
        pygame.draw.circle(win,(255,0,0),(enemy_1.hitbox_2[0]+20,enemy_1.hitbox_2[1]+40),50,2) 
    
    def hit(self):
        print('hit')
        
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
                
def redrawGameWindow():
    
    man.draw(win)
    enemy_1.draw(win)
    bullets.draw(win)
    pygame.draw.rect(win,(255,0,0),man.hitbox,2)
    
    HITBOXES=create_hitboxes(MAP_DATA, 42, 42)
    for hitbox in HITBOXES:
        pygame.draw.rect(win, (255, 0, 0), hitbox, 1) 

def update_map_data(map_data,character):
    if character.has_key:
        for row in map_data:
            if 3 in row:
                row[row.index(3)] = 0
    return map_data

def create_hitbox(length, width, x, y):
    hitbox = pygame.Rect(x, y, length, width)
    return hitbox

def create_hitboxes(map_data, hitbox_length, hitbox_width):
    global all_hitboxes
    temp_surface = pygame.Surface(win.get_size(), pygame.SRCALPHA)
    hitbox_x = 0
    hitbox_y = 0
    temp_surface.fill((0, 0, 0, 0))
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if map_data[i][j] == 4:
                hitbox = create_hitbox(hitbox_length, hitbox_width, hitbox_x, hitbox_y)
                all_hitboxes.append(hitbox)
                pygame.draw.rect(win, (255, 0, 0), hitbox, 1)
            elif map_data[i][j] == 5:
                hitbox = create_hitbox(hitbox_length, hitbox_width, hitbox_x, hitbox_y)
                all_hitboxes.append(hitbox)
                pygame.draw.rect(win, (255, 255, 0), hitbox, 1)
                if man.hitbox.colliderect(hitbox):
                    man.has_key1 = True
            elif map_data[i][j] == 3:
                hitbox = create_hitbox(hitbox_length, hitbox_width, hitbox_x, hitbox_y)
                all_hitboxes.append(hitbox)
                pygame.draw.rect(win, (255, 255, 0), hitbox, 1)
                if man.hitbox.colliderect(hitbox):
                    map_data[i][j] = 0
                    man.has_key1=True
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
enemy_1=enemy1(200,180,39,75)
run = True
shootloop=0
draw_map()
active_bullets = pygame.sprite.Group()
MAX_BULLETS = 1
bullet_sprites = pygame.sprite.Group()
player_style=pygame.image.load(r"./goku.jpg")
player_style=pygame.transform.rotozoom(player_style,0,1)
player_rect=player_style.get_rect(center=(860,503))
game_active=False
active=False
text_font=pygame.font.Font(None,50)
text1=text_font.render("GOKU THE LEGEND",False,'White')
text1_rect=text1.get_rect(center=(860,50))
text2=text_font.render("NEW GAME",False,'White')
text2_rect=text2.get_rect(center=(1610,750))
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
bar_color = 'BLUE'
border_color = BLACK
# Set the progress bar value
progress = 0.0
player_style1=pygame.image.load(r"./goku2.jpg")
player_style1=pygame.transform.rotozoom(player_style1,0,1)
player_rect1=player_style1.get_rect(center=(860,503))
game_active=False
text3=text_font.render("GOKU MADARCHOD",False,'Red')
text3_rect=text3.get_rect(center=(860,50))
text4=text_font.render("PRESS SPACE TO RUN",False,'white')
text4_rect=text4.get_rect(center=(1350,250))
while run:
    clock.tick(60)
    if(game_active):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        print(man.has_key1)
        print('------')
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
        # man.hitbox_d1=pygame.Rect(man.x,man.y,)
        
        
        
        HITBOXES=create_hitboxes(MAP_DATA, 42, 42)
        if detect_collision(man.hitbox, HITBOXES): 
            man.hitbox = handle_collision(man.hitbox,HITBOXES)
            man.x = man.hitbox[0]
            man.y = man.hitbox[1]
                
        pygame.draw.rect(win, (0, 0, 0), (0, 0, winWidth, winHeight))
        redrawGameWindow()
    elif(game_active==False):
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                exit()
            if(event.type==pygame.MOUSEBUTTONDOWN and text2_rect.collidepoint(pygame.mouse.get_pos())):
                game_active=True                    
            win.fill("black")
                #pygame.draw.ellipse(screen,'blue',pygame.Rect(615,350,500,300))
            win.blit(text1,text1_rect)
            win.blit(player_style,player_rect)
            pygame.draw.ellipse(win,'blue',pygame.Rect(1500,700,215,100))
            win.blit(text2,text2_rect)
            if progress < 2.8:
                progress += 0.01
            else:
                progress = 1.0
    if(active):
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                exit()
            if(event.key)
        win.fill("black")
        win.blit(player_style1,player_rect1)
        if():
            text3=text_font.render("Better try next time",False,'White')
            text3_rect=text3.get_rect(center=(860,740))
            win.blit(text3,text3_rect)
        
        #else:
            #text3=text_fond.render("Hemang Madarchod",False,'White')
            #text3_rect=text3.get_rect(center=(860,740))
            #screen.blit(text3,text3_rect)
        win.blit(text3,text3_rect)
        win.blit(text4,text4_rect)
    pygame.quit()
    




