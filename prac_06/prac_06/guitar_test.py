#the tests
from guitar import Guitar

CURRENT_YEAR_FOR_TEST = 2022

def main():

    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 500.0)

    expected_gibson_age = 100
    actual_gibson_age = gibson.get_age(CURRENT_YEAR_FOR_TEST)
    print(f"{gibson.name} get_age() - Expected {expected_gibson_age}. Got {actual_gibson_age}")

    expected_another_age = 9
    actual_another_age = another.get_age(CURRENT_YEAR_FOR_TEST)
    print(f"{another.name} get_age() - Expected {expected_another_age}. Got {actual_another_age}")

    expected_gibson_vintage = True
    actual_gibson_vintage = gibson.is_vintage()
    print(f"{gibson.name} is_vintage() - Expected {expected_gibson_vintage}. Got {actual_gibson_vintage}")

    expected_another_vintage = False
    actual_another_vintage = another.is_vintage()
    print(f"{another.name} is_vintage() - Expected {expected_another_vintage}. Got {actual_another_vintage}")

main()