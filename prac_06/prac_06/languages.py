#the client program
"""
CP1404/CP5632 Practical - Client code using ProgrammingLanguage
Intermediate Exercises

Estimate: 8 minutes
Start time: 2025-11-01 12:30 SGT
Finish time: 20
Actual: 2025-11-01 12:50
"""
from programing_language import ProgrammingLanguage
def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]

    print("The dynamically typed languages are: ")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == "__main__":
    main()