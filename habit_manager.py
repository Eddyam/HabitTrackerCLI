# habit_manager.py 
from habit import Habit
from data_handler import load, save_habits
import datetime

# Clase para manejar los colores de la terminal.
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'

class HabitManager: 
    def __init__(self):
        """
        Constructor del gestor. 
        Carga todos los hábitos existentes desde el archivo JSON.
        """
        self.habits = load()

    def add_habit(self, name: str, description: str = "") -> bool:
        """Añade un nuevo hábito a la lista si no existe."""
        if any(h.name.lower() == name.lower() for h in self.habits):
            print(f"Error: El hábtio {name} ya existe.")
            return False
        new_habit = Habit(name, description) # Crea nuevo objeto Habit
        self.habits.append(new_habit)
        self.save_all_habits()
        print(f"Hábito {name} añadido.")
        return True

    def save_all_habits(self):
        """Metodo interno para guardar los hábitos actuales en el archivo JSON."""
        save_habits(self.habits)