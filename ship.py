import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, alien_game):
        """Initialize the ship and set its starting position."""
        self.screen = alien_game.screen
        self.settings = alien_game.settings
        self.screen_rect : pygame.Rect = alien_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('assets/images/ship.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left + self.settings.ship_padding

        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def draw(self):
        """Draw the ship at its curent location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on movement flags."""  
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y  