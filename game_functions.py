import sys
import pygame
from time import sleep
from pygame.sprite import Sprite
from bullet import Bullet
from alien import Alien

def check_events(ship, bullets, screen, settings, stats, play_button, aliens, sb):
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y) 
    if button_clicked and not stats.game_active:
        # Reset game settings
        settings.initialise_dynamic_settings()

        # Hide the cursor
        pygame.mouse.set_visible(False)

        # Reset the game stats
        stats.reset_stats()
        stats.game_active = True
        
        # Reset scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Clear old objects
        aliens.empty()
        bullets.empty()

        # Reset fleet and ship
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

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

def get_max_columns(settings, alien_width):
    """Find out how many aliens fit on a row"""
    available_space_x = settings.screen_width - 2 * alien_width
    max_aliens_x = int(available_space_x / (2 * alien_width))
    return max_aliens_x

def get_number_rows(settings, ship_height, alien_height):
    """Find how many alien rows fit on the screen"""
    available_space_y = (
            settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(settings, screen, aliens, alien_number, row_number):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width) * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(settings, screen, ship, aliens):
    # Create an alien and find the max number of aliens
    # There is one alien width of space between each alien
    alien = Alien(settings, screen)
    max_alien_columns = get_max_columns(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(max_alien_columns):
            create_alien(settings, screen, aliens, alien_number, row_number)

def change_fleet_direction(settings, aliens):
    """Drop the fleet down and change its direction"""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1

def check_fleet_edges(settings, aliens):
    """If fleet hits edge of screen, change its direction and move it down"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def check_bullet_collisions(settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to bullet-alien collisions"""
    # Delete bullet and alien if they collide
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    check_high_score(stats, sb)

    # Create a new fleet of aliens if the old one is killed
    if len(aliens) == 0:
        bullets.empty()
        settings.increase_speed()
        create_fleet(settings, screen, ship, aliens)

        # Increase level
        stats.level += 1
        sb.prep_level()


def update_bullets(settings, screen, stats, sb, ship, aliens, bullets):
    """update bullet position and remove old bullets"""
    bullets.update()
    # Remove bullets past the top of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_collisions(settings, screen, stats, sb, ship, aliens, bullets)

def ship_hit(settings, stats, screen, sb, ship, aliens, bullets):
    """What to do when an alien 'wins'"""
    if stats.ships_left > 0:
        # Take a life
        stats.ships_left -= 1

        # Update scoreboard
        sb.prep_ships()

        # Clear list of bullets and aliens
        aliens.empty()
        bullets.empty()

        # Create a fleet and center the ship
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(settings, stats, screen, sb, ship, aliens, bullets):
    """Check if any aliens are at the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Reset as if ship was hit
            ship_hit(settings, stats, screen, sb, ship, aliens, bullets)
            break

def update_aliens(settings, stats, screen, sb, ship, aliens, bullets):
    """Check if fleet is at an edge, then update alien positions"""
    check_fleet_edges(settings, aliens)
    aliens.update()

    # Look for aliens touching player
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, sb, ship, aliens, bullets)

    # Look for aliens that have reached the bottom
    check_aliens_bottom(settings, stats, screen, sb, ship, aliens, bullets)

def update_screen(settings, ship, bullets, aliens, screen, stats, play_button, scoreboard):
    """Draws background and game elements to the window"""
    screen.fill(settings.bg_colour)
    for bullet in bullets.sprites():
        bullet.draw()
    aliens.draw(screen)
    ship.draw()

    scoreboard.show_score()

    # Draw play button before game starts
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

def check_high_score(stats, sb):
    """Check to see if there's a new high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
