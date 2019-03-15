import pygame.font

class Button():

    def __init__(self, settings, screen, message):
        """Initialise button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set properties of the button
        self.width, self.height = 200, 50
        self.button_colour = (0, 255, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once
        self.prep_message(message)

    def prep_message(self, message):
        """Turn text into a rendered image and center it on the button"""
        self.message_image = self.font.render(
            message,
            True,
            self.text_colour,
            self.button_colour
            )
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)
