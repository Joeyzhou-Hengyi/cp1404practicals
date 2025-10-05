# 1. Write name to a file
# Ask user for their name and write it to name.txt (using open/close)
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()


# 2. Read the name from the file and print greeting
# Open name.txt, read the name, then print "Hi <name>!"
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")


# 3. Read first two numbers from numbers.txt, add them, and print the result
# numbers.txt:
# 17
# 42
# 400
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
    result = number1 + number2
print(result)


# 4. Sum all numbers in numbers.txt (any number of lines)
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)