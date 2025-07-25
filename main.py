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

def main():
    """Función principal que ejecuta la aplicación."""
    manager = HabitManager() # Crea instancia del gestor de hábitos.

    while True: 
        display_menu()
        choice = input("Elige un opción: ")

        if choice == 1: 
            name = input("Nombre del hábito: ")
            description = input("Descripción (opcional)")
            manager.add_habit(name, description) # Llama al manager para añadir un hábito.
        elif choice == 2: 
            name = input("Nombre del hábito a marcar como completad: ")
            manager.complete_habit(name)
        elif choice == 3: 
            manager.list_habits()
        elif choice == 4: 
            name = input("Nombre del hábito para ver detalles: ")
            manager.show_habit_details(name)
        elif choice == 5: 
            name = input("Nombre del hábito a eliminar: ")
            manager.delete_habit(name)
        elif choice == 6: 
            manager.get_summary()
        elif choice == 7:
            print("!Hasta luego!")
            break
        else: 
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()