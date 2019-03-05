import sys
import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship

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
    aliens = Group()
    gf.create_fleet(game_settings, screen, ship, aliens)

    # Game main loop
    while True:
        gf.check_events(ship, bullets, screen, game_settings)

        # Game logic
        ship.move()
        gf.update_bullets(bullets)
        gf.update_aliens(game_settings, aliens)

        # Graphics
        gf.update_screen(game_settings, ship, bullets, aliens, screen)


run_game()
