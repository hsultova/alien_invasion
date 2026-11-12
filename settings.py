import pygame

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
        self.ship_padding = 20
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.alien_bullet_color = (155, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        self.fleet_bottom_margin = 8
        self.fleet_side_margin = 2

        # Button settings
        self.button_width, self.button_height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.button_font = pygame.font.SysFont(None, 48)

        self.speedup_scale = 1.5
        self.score_scale = 2.0

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 5.0
        self.bullet_speed = 4.5
        self.alien_bullet_speed = -4.5
        self.alien_speed = 1.0
        self.alien_fire_ms = 5000
        self.shooters = 1

        # fleet direction 1 -> right; -1 -> left
        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

        self.alien_fire_ms = int(self.alien_fire_ms / self.speedup_scale)
        self.shooters = self.shooters + 1