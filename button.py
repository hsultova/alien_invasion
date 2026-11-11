import pygame

from settings import Settings

class Button:
    """A class to build buttons for the game."""

    def __init__(self, screen: pygame.Surface, settings: Settings, message) -> None:
        """Initialize button attributes."""

        self.screen = screen
        self.settings = settings
        self.screen_rect = self.screen.get_rect()

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, settings.button_width, settings.button_height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once
        self._prep_message(message)

    def _prep_message(self, message):
        """Turn message into a rendered image and center text on the button."""
        self.message_image = self.settings.button_font.render(message, True, self.settings.text_color, self.settings.button_color)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.screen_rect.center

    def draw(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)