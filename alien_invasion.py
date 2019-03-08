import sys
import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats

def run_game():
    # Initialise game, settings, and create a screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((
        game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption(game_settings.caption)

    # Stats object
    stats = GameStats(game_settings)

    # Setup game elements
    ship = Ship(game_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(game_settings, screen, ship, aliens)

    # Game main loop
    while True:
        gf.check_events(ship, bullets, screen, game_settings)

        if stats.game_active:
            # Do game logic if the player hasn't lost
            ship.move()
            gf.update_bullets(game_settings, screen, ship, aliens, bullets)
            gf.update_aliens(game_settings, stats, screen, ship, aliens, bullets)

        # Graphics
        gf.update_screen(game_settings, ship, bullets, aliens, screen)


run_game()
