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

    def show_habit_details(self, habit_name: str) -> bool: 
        """Muestra la descripción y el historial de completitud de un hábito especifico."""
        for habit in self.habits:
            if habit.name.lower() == habit_name.lower():
                print(f"\n--- Detalle del Hábito: {Colors.BLUE}{habit.name}{Colors.ENDC} ---")
                print(f"Descripción: {habit.description if habit.description else 'N/A'}")
                if not habit.completions:
                    print("Este hábito aun no ha sido completado.")
                else:
                    print("Historial de completitud:")
                    # Ordena de la mas reciente a la mas antigua
                    for ts in sorted(habit.completions, reverse=True):
                        print(f"    - {ts.strftime('%Y-%m-%d %H:%M:%S')}")
                print("-------------------")
                return True
            print(f"Error: Hábito {habit_name} no encontrado.")
            return False
    
    def delete_habit(self, habit_name: str) -> bool:
        """Elimina un hábito de la lista"""
        initial_len = len(self.habits)
        # Crea nueva lista excluyendo el hábito a borrar
        self.habits = [h for h in self.habits if h.name.lower() != habit_name.lower()]
        if len(self.habits) < initial_len: 
            self.save_all_habits()
            print(f"Hábito {habit_name} eliminado.")
            return True
        print(f"Error: Hábito {habit_name} no encontrado para eliminar.")
        return False

    def get_summary(self):
        """Genera y muestra un resumen general de todos los hábitos."""
        if not self.habits:
            print("No hay hábitos para resumir.")
        
        print("\n--- Resumen General de Hábitos ---")
        for habit in self.habits:
            last_completion = "Nunca"
            if habit.completions:
                last_completion_dt = max(habit.completions) # Completitud mas reciente
                last_completion = last_completion_dt.strftime('%Y-%m-%d %H:%M:%S')
            
            print(f"Hábito: {habit.name}")
            print(f" - Completado: {len(habit.completions)} veces")
            print(f" - Último registro: {last_completion}")
            print("---")
        print("----------------------------")

    def save_all_habits(self):
        """Metodo interno para guardar los hábitos actuales en el archivo JSON."""
        save_habits(self.habits)