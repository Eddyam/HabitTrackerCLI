# habit.py
import datetime

class Habit:
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.completions = [] # Fecha y hora en la que se completo el habito.

