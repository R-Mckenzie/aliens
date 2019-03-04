import sys
import pygame
from bullet import Bullet

def check_events(ship, bullets, screen, settings):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            check_ship_keydown(event, ship)
            check_bullet_keydown(event, ship, bullets, settings, screen)
        elif event.type == pygame.KEYUP:
            check_ship_keyup(event, ship)

def check_ship_keydown(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_ship_keyup(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_bullet_keydown(event, ship, bullets, settings, screen):
    """Fire if space pressed and bullet limit not reached"""
    if event.key == pygame.K_SPACE and len(bullets) < settings.max_bullets:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
    """update bullet position and remove old bullets"""
    bullets.update()
    # Remove bullets past the top of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_screen(settings, ship, bullets, alien, screen):
    """Draws background and game elements to the window"""
    screen.fill(settings.bg_colour)
    for bullet in bullets.sprites():
        bullet.draw()
    ship.draw()
    alien.draw()
    pygame.display.flip()
