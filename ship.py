import pygame

class Ship():

    def __init__(self, settings,  screen):
        """Initialise the ship and set it's position"""
        self.screen = screen

        # Setup image
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Center ship at bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        # Movement variables
        self.speed = settings.ship_speed
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def move(self):
        """Updates ship position base on input flags
        self.center is used enable finer speed control"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.speed

        # Updade pygame rect center from our float center
        self.rect.centerx = self.center

    def draw(self):
        self.screen.blit(self.image, self.rect)
