"""File to define Bear class."""


class Bear:
    """Creating the bear class."""

    age: int = 0
    hunger_score: int = 0

    def __init__(self):
        """Initializer of bear class."""
        self.hunger_score: int = 0
        self.age: int = 0
        return None
    
    def one_day(self):
        """Simulates one day on the river."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Updates the bears hunger score based on the number of fish eaten."""
        self.hunger_score += num_fish