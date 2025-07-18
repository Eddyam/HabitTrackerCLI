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
    
    def to_dict(self):
        """
        Convierte el objeto habit en un diccionario.
        Sirve para guardar los datos en formato JSON. 
        """
        return {
            "name": self.name,
            "description": self.description,
            "completions": [ts.isoformat() for ts in self.completions] # Convierte datetime a cadena ISO
        }
    
    def from_dict(cls, data: dict):
        # Convertir JSON a datetime
        name = data.get("name")
        description = data.get("description", "")
        habit = cls(name, description)
        habit.completions = [datetime.datetime.fromisoformat(ts) for ts in data.get("completions", [])]
        return habit