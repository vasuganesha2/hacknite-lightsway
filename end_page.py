import pygame
import sys
pygame.init()
text_font=pygame.font.Font(None,50)
text_font=pygame.font.Font(None,50)
clock=pygame.time.Clock()
screen=pygame.display.set_mode((1721,1007))
player_style1=pygame.image.load(r"./goku2.jpg")
player_style1=pygame.transform.rotozoom(player_style1,0,1)
player_rect1=player_style1.get_rect(center=(860,503))
game_active=False
text3=text_font.render("GOKU MADARCHOD",False,'Red')
text3_rect=text3.get_rect(center=(860,50))
text4=text_font.render("PRESS SPACE TO RUN",False,'white')
text4_rect=text4.get_rect(center=(1350,250))
while True:
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            pygame.quit()
            exit()
    screen.fill("black")
    screen.blit(player_style1,player_rect1)
    #if(condition):
        #text3=text_fond.render("Better try next time",False,'White')
        #text3_rect=text3.get_rect(center=(860,740))
        #screen.blit(text3,text3_rect)
    
    #else:
        #text3=text_fond.render("Hemang Madarchod",False,'White')
        #text3_rect=text3.get_rect(center=(860,740))
        #screen.blit(text3,text3_rect)
    screen.blit(text3,text3_rect)
    screen.blit(text4,text4_rect)
    pygame.display.update() 
    clock.tick(60)