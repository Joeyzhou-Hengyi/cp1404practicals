"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}

def main():
    print(CODE_TO_NAME)
    state_code = input("Enter short state: ").strip()

    while state_code != "":
        try:
            # Convert to uppercase for dictionary lookup
            print(f"{state_code.upper()} is {CODE_TO_NAME[state_code.upper()]}")
        except KeyError:
            print("Invalid short state")

        state_code = input("Enter short state: ").strip()

    # Print all states neatly when finished
    print("\nAll states and names:")
    key_width = max(len(k) for k in CODE_TO_NAME)
    for code, name in sorted(CODE_TO_NAME.items()):
        print(f"{code:{key_width}} is {name}")

main()
