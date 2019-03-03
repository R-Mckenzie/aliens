import pygame

class Ship():

    def __init__(self, screen):
        """Initialise the ship and set it's position"""
        self.screen = screen

        # Setup image
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Center ship at bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def draw(self):
        self.screen.blit(self.image, self.rect)
