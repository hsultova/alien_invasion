import pygame
from pygame.sprite import Sprite

from settings import Settings
from ship import Ship

class Bullet(Sprite):
    """Manage bullets fired from the ship."""

    def __init__(self, screen: pygame.Surface, settings: Settings, ship: Ship  ) -> None:
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.color = self.settings.bullet_color

        self.rect: pygame.Rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw(self):
        """Draw the bullet at its curent location"""
        pygame.draw.rect(self.screen, self.color, self.rect)