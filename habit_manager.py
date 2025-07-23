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
    
    def complete_habit(self, habit_name: str) -> bool: 
        """Marca un hábito existente como completado con la fecha y hora actuales."""
        for habit in self.habits: 
            if habit.name.lower() == habit_name.lower():
                habit.add_completion()
                self.save_all_habits()
                print(f"Hábito {habit_name} marcado como completado en {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.")
                return True
        print(f"Error: Hábito {habit_name} no encontrado.")

    def list_habits(self):
        """Imprime la lista de todos los hábitos y cuantas veces se han completado."""
        if not self.habits:
            print("No hay hábitos registrados todavía.")
            return
        print("\n----Tus hábitos ----")
        for i, habit in enumerate(self.habits):
            print(f"{i + 1}. {habit.name} ({len(habit.completions)} veces completado.)")
        print("-------------------")

    def save_all_habits(self):
        """Metodo interno para guardar los hábitos actuales en el archivo JSON."""
        save_habits(self.habits)