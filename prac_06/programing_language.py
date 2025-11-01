#the class
"""
CP1404/CP5632 Practical - ProgrammingLanguage class
Intermediate Exercises

Estimate: 10 minutes
Start time: 2025-11-01 12:00 SGT
Finish time: 2025-11-01 12:30
Actual: 30
"""
class ProgrammingLanguage:
    def _init_(self, name: str, typing:str, reflection: bool, year: int):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return str(self.typing).strip().lower() == "dynamic"



