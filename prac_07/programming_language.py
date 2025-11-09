"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """
        Initialize a ProgrammingLanguage instance.

        :param name: Language name (e.g. 'Python')
        :param typing: 'Dynamic' or 'Static'
        :param reflection: Boolean, True if supports reflection
        :param year: Year of creation (int)
        :param pointer_arithmetic: Boolean, True if supports pointer arithmetic
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"
    def has_pointer_arithmetic(self):
        """Return true if this language supports pointer arithmetic"""
        return bool(self.pointer_arithmetic)

    def __str__(self):
        """Return a nicely formatted string for the language."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"Year={self.year}, PointerArithmetic={self.pointer_arithmetic}")


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()