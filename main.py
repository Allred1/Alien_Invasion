import sys
import pygame

# import the classes
from settings import Settings
from ship import Ship



def run_game():
    # Initialize pygame, settings, and screen object. 
    pygame.init()
    ai_settings = Settings()    # Instance of Settings class
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))      # accessing the attributes of the Settings class
    pygame.display.set_caption("Alien Invasion")


    # Make a ship
    ship = Ship(screen)


    # Start the main loop for the game
    while True: 
        # Watch for keyboard and mouse events. 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass hrough the loop. 
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()
    

run_game()