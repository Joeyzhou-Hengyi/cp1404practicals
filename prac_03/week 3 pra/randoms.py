import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Answers (in comments):
# Line 1: produced a random integer between 5 and 20 inclusive.
# Smallest: 5, Largest: 20

# Line 2: produced a random number between 3 and 9 with a step of 2 (so 3, 5, 7, or 9)
# Could it produce a 4? No.

# Line 3: produced a random floating-point number between 2.5 and 5.5
# Smallest: 2.5, Largest: 5.5

# Random number between 1 and 100 inclusive:
print(random.randint(1, 100))