# main. py
from habit_manager import HabitManager
from pathlib import Path

class Colors: # Define colores para la terminal
    GREEN = "\033[92m"
    ENDC = "\033[0m" # Resetea el color

def display_menu():
    """Muestra el menú de opciones al usuario."""
    print(Colors.GREEN + "\n--- GESTOR DE HÁBITOS ---" + Colors.ENDC)
    print("1. Añadir Hábito")
    print("2. Marcar Hábito como Completado")
    print("3. Listar Hábitos")
    print("4. Ver Detalle del Hábito")
    print("5. Eliminar Hábito")
    print("6. Resumen General")
    print("7. Salir")
    print(Colors.GREEN + "----------------------------" + Colors.ENDC)