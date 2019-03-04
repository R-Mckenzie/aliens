import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialise game, settings, and create a screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((
        game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption(game_settings.caption)

    # Setup game elements
    ship = Ship(game_settings, screen)
    bullets = Group()

    # Game main loop
    while True:
        gf.check_events(ship, bullets, screen, game_settings)

        # Game logic
        ship.move()
        gf.update_bullets(bullets)

        # Graphics
        gf.update_screen(game_settings, ship, bullets, screen)


run_game()
