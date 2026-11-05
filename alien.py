import pygame
from pygame.sprite import Sprite

from settings import Settings

class Alien(Sprite):
    """Class that represent an alien ship."""

    def __init__(self, screen: pygame.Surface, settings: Settings) -> None:
        """Initializes an alian ship and set its starting position."""

        super().__init__()
        self.screen = screen
        self.settings = settings

        # Load the alian ship image and get its rect
        self.image = pygame.image.load('assets/images/alien.png')
        self.rect: pygame.Rect = self.image.get_rect()

        # Start each new alien ship near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self) -> bool:
        """Check if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self) -> None:
        """Move the alien right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
