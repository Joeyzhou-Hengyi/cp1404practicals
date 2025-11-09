class Guitar:
    """Represent a Guitar with name, year, and cost."""

    def __init__(self, name: str, year: int, cost: float):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other: "Guitar"):
        """Order guitars by year (older comes first)."""
        return self.year < other.year

    def is_vintage(self, current_year: int = 2025):
        return current_year - self.year >= 50
