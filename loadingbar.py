import pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the dimensions of the screen
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

# Set the font and size
font = pygame.font.Font(None, 36)

# Set the progress bar position and size
bar_pos = (50, 50)
bar_width = 600
bar_height = 20

# Set the progress bar color and border color
bar_color = GREEN
border_color = BLACK

# Set the progress bar value
progress = 0.0

# Run the game loop
done = False
clock = pygame.time.Clock()

while not done:
    # --- Event processing ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic ---
    # Increment the progress bar value
    if(progress<1):
        progress += 0.01
    # --- Drawing ---
    # Clear the screen
    screen.fill(WHITE)

    # Draw the progress bar border
    pygame.draw.rect(screen, border_color, [bar_pos[0], bar_pos[1], bar_width, bar_height], 2)

    # Draw the progress bar
    pygame.draw.rect(screen, bar_color, [bar_pos[0], bar_pos[1], bar_width * progress, bar_height])

    # Draw the progress percentage
    progress_text = font.render("{:.0%}".format(progress), True, BLACK)
    screen.blit(progress_text, (bar_pos[0] + bar_width / 2 - progress_text.get_width() / 2, bar_pos[1] + bar_height + 10))

    # Update the screen
    pygame.display.update()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Quit the game
pygame.quit()
