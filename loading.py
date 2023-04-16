import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Loading...")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up font
font = pygame.font.SysFont(None, 30)

# Set up loading spinner
spinner_width = 50
spinner_radius = spinner_width // 2
spinner_center = (screen_width // 2, screen_height // 2)
spinner_angle = 0
spinner_speed = 0.1

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with white
    screen.fill(WHITE)
    
    # Draw the loading spinner
    spinner_outline = pygame.Rect(spinner_center[0] - spinner_radius, spinner_center[1] - spinner_radius, spinner_width, spinner_width)
    pygame.draw.arc(screen, 'GREY', spinner_outline, 0, math.pi * 2, 3)
    spinner_angle += spinner_speed
    spinner_pivot = (spinner_center[0] + spinner_radius * math.cos(spinner_angle), spinner_center[1] + spinner_radius * math.sin(spinner_angle))
    pygame.draw.line(screen, BLUE, spinner_center, spinner_pivot, 3)
    # Draw the loading text
    loading_text = "Loading"
    loading_text += "." * ((pygame.time.get_ticks() // 500) % 4)
    loading_surface = font.render(loading_text, True, BLACK)
    loading_rect = loading_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
    screen.blit(loading_surface, loading_rect)
    
    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
