import pygame
from pygame.sprite import Sprite

from settings import Settings

class Bullet(Sprite):
    """Manage bullets fired from the ship."""

    def __init__(self, screen: pygame.Surface, settings: Settings, x, y, speed, color) -> None:
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.speed = speed
        self.color = color

        self.rect: pygame.Rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = (x, y)

        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self):
        """Draw the bullet at its curent location"""
        pygame.draw.rect(self.screen, self.color, self.rect)