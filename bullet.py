import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """Manage bullets fired from the ship."""

    def __init__(self, alien_game):
        super().__init__()
        self.screen = alien_game.screen
        self.settings = alien_game.settings
        self.colr = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = alien_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw(self):
        """Draw the bullet at its curent location"""
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)