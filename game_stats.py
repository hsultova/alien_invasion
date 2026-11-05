from settings import Settings

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, settings: Settings) -> None:
        """Initialize statistics."""
        self.settings = settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ship_left = self.settings.ship_limit