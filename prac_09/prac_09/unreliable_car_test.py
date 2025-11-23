# unreliable_car_test.py
"""
Test the UnreliableCar class.
"""
from unreliable_car import UnreliableCar
def main():
    # Create a few cars with different reliability
    reliable_car = UnreliableCar("Almost Perfect Car", 100, 90)   # 90% 可靠
    unreliable_car = UnreliableCar("Dodgy Car", 100, 30)          # 30% 可靠

    print("Testing UnreliableCar behaviour with multiple drive attempts...\n")

    # Test the 90% reliable car
    print("=== 90% Reliable Car ===")
    total_attempts = 10
    total_distance_driven = 0
    for i in range(1, total_attempts + 1):
        distance = reliable_car.drive(10)  # try to drive 10 km each time
        total_distance_driven += distance
        print(f"Attempt {i}: Drove {distance} km (odometer={reliable_car.odometer}, fuel={reliable_car.fuel})")
    print(f"Total distance driven (expected to be high): {total_distance_driven} km\n")

    # Test the 30% reliable car
    print("=== 30% Reliable Car ===")
    total_attempts = 10
    total_distance_driven = 0
    for i in range(1, total_attempts + 1):
        distance = unreliable_car.drive(10)  # try to drive 10 km each time
        total_distance_driven += distance
        print(f"Attempt {i}: Drove {distance} km (odometer={unreliable_car.odometer}, fuel={unreliable_car.fuel})")
    print(f"Total distance driven (expected to be much lower): {total_distance_driven} km")


if __name__ == "__main__":
    main()