import sys
import pygame
from settings import Settings

def run_game():
    # Initialise game, settings, and create a screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption(game_settings.caption)

    # Game main loop
    while True:
        # Collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Graphics
        screen.fill(game_settings.bg_colour)
        pygame.display.flip()


run_game()
