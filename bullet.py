import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Defines bullets fired from a ship"""

    def __init__(self, settings, screen, ship):
        """Create a new bullet at ship's position"""
        super().__init__()
        self.screen = screen

        # Create a rect at correct position
        self.rect = pygame.Rect(
                ship.rect.centerx,
                ship.rect.top,
                settings.bullet_width,
                settings.bullet_height
                )

        # Store position as a decimal value for finer speed control
        self.y = float(self.rect.y)

        self.colour = settings.bullet_colour
        self.speed = settings.bullet_speed

    def update(self):
        """Move the bullet up the screen. 'self.y' is the position as a float"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)

