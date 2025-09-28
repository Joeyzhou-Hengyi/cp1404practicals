def main():
    print("Temperature Converter")
    print("(C)elsius to Fahrenheit")
    print("(F)ahrenheit to Celsius")
    choice = input("Choose (C/F): ").strip().upper()

    if choice == "C":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F")
    elif choice == "F":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit:.1f}°F = {celsius:.1f}°C")
    else:
        print("Invalid choice")


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


main()