import json

from settings import Settings

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, settings: Settings) -> None:
        """Initialize statistics."""
        self.settings = settings

        self.read_high_score()
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def write_high_score(self):
        """Write the high score to a file."""
        with open('game_stats.txt', 'w', encoding="utf-8") as file:
            file.write(json.dumps(f"score: {self.high_score}"))

    def read_high_score(self):
        """Read the high score from a file."""
        with open('game_stats.txt', 'r', encoding="utf-8") as file:
            score_from_file = file.read()
            if score_from_file:
                self.high_score = int(score_from_file.split(": ")[1].strip('"'))
            else:
                self.high_score = 0