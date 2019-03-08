import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Graphics
        self.image = pygame.image.load('images/alien.bmp').convert()
        self.rect = self.image.get_rect()

        # Starting position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Position as float
        self.x = float(self.rect.x)

    def check_edges(self):
        """returns true if the alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        return False

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the alien"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
