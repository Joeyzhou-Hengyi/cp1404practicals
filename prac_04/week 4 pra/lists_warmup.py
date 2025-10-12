
numbers = [3, 1, 4, 1, 5, 9, 2]

# --- Predict the values (without running the code) ---

# numbers[0]      → 3
# numbers[-1]     → 2
# numbers[3]      → 1
# numbers[:-1]    → [3, 1, 4, 1, 5, 9]
# numbers[3:4]    → [1]
# 5 in numbers    → True
# 7 in numbers    → False
# "3" in numbers  → False   (because "3" is a string, not an integer)
# numbers + [6, 5, 3] → [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


# Change the first element to "ten" (string)
numbers[0] = "ten"

# Change the last element to 1
numbers[-1] = 1

# Print all elements except the first two
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)