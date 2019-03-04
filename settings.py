class Settings():
    """Stores settings for the game"""

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)
        self.caption = "Alien Invasion"

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.max_bullets = 3
