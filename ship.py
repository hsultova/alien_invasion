import pygame

from pygame.sprite import Sprite

from settings import Settings

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, screen: pygame.Surface, settings: Settings) -> None:
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.screen_rect : pygame.Rect = screen.get_rect()

        # Load the ship image and get its rect
        self.image: pygame.Surface = pygame.image.load('assets/images/ship.png')
        self.rect: pygame.Rect = self.image.get_rect()

        self.cente_ship()

        self.moving_right = False
        self.moving_left = False

    def draw(self):
        """Draw the ship at its curent location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on movement flags."""  
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def cente_ship(self):
        """Center the ship on the screen"""
        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - self.settings.ship_padding
        self.x = float(self.rect.x)