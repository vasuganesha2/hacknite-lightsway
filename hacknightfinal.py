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

text_b=texta.get_rect(center=(860,480))
# Set the font and size
font = pygame.font.Font(None, 36)
# Set the progress bar position and size
bar_pos = (50, 50)
bar_width = 600
bar_height = 20
# Set the progress bar color and border color
bar_color = 'RED'
border_color = 'BLACK'
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
black = (0, 0, 0)
white = (255, 255, 255)

# Define the font and text for the settings button
button_font = pygame.font.SysFont(None, 30)
settings_text = button_font.render("Settings", True, black)

# Define the settings button
settings_button = settings_text.get_rect()
settings_button.bottomright = (1700,950)

# Set the initial state of the game
settings_open = False
while True:
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            pygame.quit()
            exit()
        if(event.type==pygame.MOUSEBUTTONDOWN and text2_rect.collidepoint(pygame.mouse.get_pos())):
            active=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()

                # Check if the mouse click is inside the settings button
                if settings_button.collidepoint(mouse_position):
                    settings_open = not settings_open
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
            active=True
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
        pygame.draw.rect(screen, black, settings_button, 2)
        screen.blit(settings_text, settings_button)
        if settings_open:
        # Draw a translucent overlay to darken the screen
            overlay = pygame.Surface((1721,1000), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 128))
            screen.blit(overlay, (0, 0))

        # Draw the settings menu
            settings_menu = pygame.Surface((500, 400))
            settings_menu.fill(white)
            settings_menu_rect = settings_menu.get_rect()
            settings_menu_rect.center = (860,503)
            pygame.draw.rect(settings_menu, black, (0, 0, 500, 400), 2)
            screen.blit(settings_menu, settings_menu_rect)
    # Update the screen
    pygame.display.update()
    clock.tick(60)