# silver_service_taxi.py
"""
SilverServiceTaxi class, derived from Taxi
"""
from taxi import Taxi
class SilverServiceTaxi(Taxi):
    """Specialised Taxi with fanciness and flagfall."""

    flagfall = 4.50  # class variable: extra charge per fare

    def __init__(self, name, fuel, fanciness):
        """
        Initialise a SilverServiceTaxi instance.
        """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # base price from Taxi class variable, then scale for this object
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """
        Calculate the fare for the current trip.
        Use the parent Taxi fare calculation, then add flagfall.
        """
        base_fare = super().get_fare()
        return base_fare + self.flagfall

    def __str__(self):
        """Return string representation including flagfall."""
        # super().__str__() should already include name, fuel, odo, distance, and $/km
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"