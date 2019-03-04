import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Represents a single alien"""

    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Graphics
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Starting position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Position as float
        self.x = float(self.rect.x)

    def draw(self):
        self.screen.blit(self.image, self.rect)
