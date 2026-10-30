import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, alien_game):
        """Initialize the ship and set its starting position."""
        self.screen = alien_game.screen
        self.screen_rect : pygame.Rect = alien_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('assets/images/ship.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def draw(self):
        """Draw the ship at its curent location"""
        self.screen.blit(self.image, self.rect)