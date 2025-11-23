# unreliable_car.py
"""
UnreliableCar class that inherits from Car.
"""
import random
from car import Car

class UnreliableCar(Car):
    """Specialised Car that sometimes does not drive as expected."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_chance = random.uniform(0, 100)  # temporary value, not stored as self attribute
        if random_chance < self.reliability:
            # Car works as expected this time
            return super().drive(distance)
        # Car fails to drive this time
        return 0