# silver_service_taxi_test.py
"""
Tests for the SilverServiceTaxi class.
"""
from silver_service_taxi import SilverServiceTaxi
def main():
    # Create a SilverServiceTaxi with fanciness of 2
    fancy_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    # Start a new fare and drive 18 km
    fancy_taxi.start_fare()
    fancy_taxi.drive(18)
    fare = fancy_taxi.get_fare()
    print(f"Fare for 18 km trip (fanciness=2): ${fare:.2f}")
    # Assert test: expected fare is 48.78
    # 1.23 * 2 = 2.46 per km; 2.46 * 18 = 44.28; + 4.50 flagfall = 48.78
    assert abs(fare - 48.78) < 0.01, f"Expected fare ~48.78, got {fare}"
    # Also check the __str__ looks reasonable (可选)
    print(fancy_taxi)

if __name__ == "__main__":
    main()