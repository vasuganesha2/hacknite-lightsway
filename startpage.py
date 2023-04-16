import pygame
import sys
pygame.init()
text_font=pygame.font.Font(None,50)
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
# Run the game loop
done = False
while True:
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            pygame.quit()
            exit()
        if(event.type==pygame.MOUSEBUTTONDOWN and text2_rect.collidepoint(pygame.mouse.get_pos())):
            active=True                    
    screen.fill("black")
    #pygame.draw.ellipse(screen,'blue',pygame.Rect(615,350,500,300))
    screen.blit(text1,text1_rect)
    screen.blit(player_style,player_rect)
    pygame.draw.ellipse(screen,'blue',pygame.Rect(1500,700,215,100))
    screen.blit(text2,text2_rect)
    if progress < 2.8:
        progress += 0.01
    else:
        progress = 1.0
        #pygame.draw.rect(screen, border_color, [bar_pos[0], bar_pos[1], bar_width, bar_height], 2)

    # Draw the progress bar
    #pygame.draw.rect(screen, bar_color, [bar_pos[0], bar_pos[1]+850, bar_width * progress, bar_height])

    # Draw the progress percentage
    #progress_text = font.render("{:.0%}".format(progress), True, BLACK)
    #screen.blit(progress_text, (bar_pos[0] + bar_width / 2 - progress_text.get_width() / 2-250, bar_pos[1] + bar_height + 850))
    pygame.display.update()
    clock.tick(60)
    #if(active):
    #condition