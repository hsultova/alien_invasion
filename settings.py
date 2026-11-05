class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)
        
        self.framerate = 60

        # Ship settings
        self.ship_speed = 5.5
        self.ship_padding = 20

        # Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction 1 -> right; -1 -> left
        self.fleet_direction = 1
        self.fleet_bottom_margin = 6
        self.fleet_side_margin = 2
        self.ship_limit = 3