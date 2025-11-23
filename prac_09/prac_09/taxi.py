# taxi.py
"""
Taxi class, derived from Car
"""
from car import Car

class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    price_per_km = 1.23  # CLASS VARIABLE — shared by all Taxis

    def __init__(self, name, fuel):
        """Initialise a Taxi."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return string representation of a Taxi."""
        return f"{super().__str__()}, fare distance = {self.current_fare_distance}"

    def get_fare(self):
        """Return the cost of the fare."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but track fare distance."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven