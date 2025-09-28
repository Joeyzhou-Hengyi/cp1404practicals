import random


def main():
    print("Welcome to the Score Menu Program")
    score = get_valid_score()

    choice = ""
    while choice != "Q":
        print_menu()
        choice = input(">>> ").strip().upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(evaluate_score(score))
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell! Thanks for using the program.")
        else:
            print("Invalid choice. Please try again.")


def print_menu():
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    score = float(input("Enter a valid score (0–100): "))
    while score < 0 or score > 100:
        print("Invalid score, must be between 0 and 100 inclusive.")
        score = float(input("Enter a valid score (0–100): "))
    return score


def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print("*" * int(score))


main()
