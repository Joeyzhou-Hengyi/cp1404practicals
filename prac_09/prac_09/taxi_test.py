# taxi_test.py
"""
Test file for the Taxi class.
"""
from taxi import Taxi
my_taxi = Taxi("Prius 1", 100)

# Drive the taxi 40 km
my_taxi.drive(40)

# Print details and current fare
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")

# Restart the fare
my_taxi.start_fare()

# Drive 100 km
my_taxi.drive(100)

# Print details and current fare again
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")