import pygame

pygame.init()
# Set up the Pygame window
window_size = (1721,1007)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Settings Button Example")

# Define the colors to be used
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
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Check for mouse click events
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()

            # Check if the mouse click is inside the settings button
            if settings_button.collidepoint(mouse_position):
                settings_open = not settings_open

    # Set the screen background
    screen.fill(white)

    # Draw the settings button
    pygame.draw.rect(screen, black, settings_button, 2)
    screen.blit(settings_text, settings_button)

    # Draw the settings menu if it is open
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

