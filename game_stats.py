import alien_invasion

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, alien_game: alien_invasion.AlienInvasion) -> None:
        """Initialize statistics."""
        self.settings = alien_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ship_left = self.settings.ship_limit