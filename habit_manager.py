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