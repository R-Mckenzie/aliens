class GameStats():
    """Tracks statistics for the game"""

    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()

        # High score should never reset
        self.high_score = 0

        # Start the game in an active state
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
