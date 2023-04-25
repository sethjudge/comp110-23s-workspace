"""File to define River class."""


__author__ = "730569838"


from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Creating the river class."""
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking the ages of the bears and fish and determining if they should be removed from the river."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]
        return None

    def bears_eating(self):
        """If enough fish are in the river, the bear will eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Checks how hungry the bear is and removes them if their hunger score is below 0."""
        alive_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                alive_bears.append(bear)
        self.bears = alive_bears
        return None
        
    def repopulate_fish(self):
        """Has each pair of fish produce 4 offspring."""
        fish_count = len(self.fish)
        offspring_count = (fish_count // 2) * 4
        new_fish = [Fish() for fish in range(offspring_count)]
        self.fish += new_fish
        return None
    
    def repopulate_bears(self):
        """Has each pair of bears produce 1 offspring."""
        bear_count = len(self.bears)
        offspring_count = bear_count // 2
        for i in range(offspring_count):
            new_bear = Bear()
            self.bears.append(new_bear)
        return None
    
    def view_river(self):
        """Shows the status of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        """Simulates one week of life in the river."""
        days: int = 0
        days_in_week: int = 7
        for days in range(days_in_week):
            days += 1
            self.one_river_day()
        return None

    def remove_fish(self, amount: int):
        """Remove frontmost fish from the river."""
        for idx in range(amount):
            self.fish.pop(0)
        return None