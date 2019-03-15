class Settings():
    """Stores settings for the game"""

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)
        self.caption = "Alien Invasion"

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.max_bullets = 3

        # Alien settings
        self.fleet_drop_speed = 10
        self.alien_points = 50

        # Difficulty settings
        self.speedup_scale = 1.3
        self.score_scale = 1.5

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 2
        self.alien_speed = 1

        # Direction of the fleet. -1 is left; 1 is right
        self.fleet_direction = 1

    def increase_speed(self):
        """Increases the speed (and points) as game progresses"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
