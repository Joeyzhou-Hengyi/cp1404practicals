#the class
from datetime import datetime

class Guitar:
    """Represent a Guitar with name, year and cost."""
    VINTAGE_AGE = 50

    def __init__(self, name: str, year: int, cost: float):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self, current_year: int | None = None):
        """Return the guitar's age."""
        if current_year is None:
            current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is vintage (age >= VINTAGE_AGE)."""
        return self.get_age() >= Guitar.VINTAGE_AGE

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"