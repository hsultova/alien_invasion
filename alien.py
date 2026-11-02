import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class that represent an alien ship."""

    def __init__(self, alien_game):
        """Initializes an alian ship and set its starting position."""

        super().__init__()
        self.screen = alien_game.screen

        # Load the alian ship image and get its rect
        self.image = pygame.image.load('assets/images/alien.png')
        self.rect = self.image.get_rect()

        # Start each new alien ship near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
