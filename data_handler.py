# data_handler.py
import json
from pathlib import Path
from habit import Habit

FILE_PATH = Path("habits.json") # Ruta del archivo JSON. 

def load() -> list[Habit]:
    """
    Carga los hábitos desde el archivo JSON y los convierte en una lista de objetos.
    """
    if not FILE_PATH.exists():
        return []
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f) # Carga el contenido del JSON
            # Convierte cada diccionario a objetos.
            return [Habit.from_dict(item) for item in data]
    except json.JSONDecodeError:
        print("Error: El archivo habits.json está corrupto o vacio. Se iniciará con hábitos vacios.")
        return []

def save_habits(habits: list[Habit]):
    """
    Guarda una lista de objetos Habit en el archivo JSON.
    """
    data_to_save = [habit.to_dict() for habit in habits]
    with open(FILE_PATH, 'w', encoding='utf-8') as f: 
        json.dump(data_to_save, f, indent=4) # Escribe la lista de diccionarios en el archivo.