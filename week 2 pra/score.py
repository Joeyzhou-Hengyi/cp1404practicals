
import random


def main():
    score = float(input("Enter your score (0–100): "))
    result = evaluate_score(score)
    print(result)

    # Part 2: Random score
    random_score = random.randint(0, 100)
    print(f"\nRandom score: {random_score}")
    print(evaluate_score(random_score))


def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()