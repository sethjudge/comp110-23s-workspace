"""File to define Fish class."""


class Fish:
    """Creating the fish class."""
    
    def __init__(self):
        """Initializing the fish class."""
        self.age: int = 0
        return None
    
    def one_day(self):
        """Simulates aging from one day on the river."""
        self.age += 1
        return None