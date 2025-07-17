# habit.py
import datetime

class Habit:
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.completions = [] # Fecha y hora en la que se completo el habito.

    def add_completion(self, timestap: datetime.datetime = None):
        """Añade una marca de tiempo de completid al habito."""
        if timestap is None:
            timestap = datetime.datetime.now() # Usa hora actual, si no se prporciona hora.
        self.completions.append(timestap) # Añade fecha y hora a la lista

    def __str__(self):
        """Representa el objeto como una cadena legible."""
        return f"Hábito: {self.name} - Descripcion: {self.description} - Completado {len(self.completions)} veces."