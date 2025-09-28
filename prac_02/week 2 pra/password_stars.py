MIN_LENGTH = 5

password = input("Enter a password: ")
while len(password) < MIN_LENGTH:
    print(f"Password must be at least {MIN_LENGTH} characters long")
    password = input("Enter a password: ")

print('*' * len(password))

MIN_LENGTH = 5

def main():
    password = input("Enter a password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long")
        password = input("Enter a password: ")

    print('*' * len(password))

main()

MIN_LENGTH = 5

def main():
    password = get_password()
    print_stars(password)


def get_password():
    password = input("Enter a password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long")
        password = input("Enter a password: ")
    return password


def print_stars(password):
    print('*' * len(password))


main()