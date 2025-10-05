"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
"""
When will a ValueError occur?
When the user enters data that cannot be converted to a number (e.g., "abc" for int()).
When will a ZeroDivisionError occur?
When the denominator is 0 and we attempt numerator / denominator.
Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes. Validate the denominator (re-prompt until it's non-zero) before doing the division.

"""