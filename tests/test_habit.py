# tests/test_habit.py
import datetime
from habit import Habit

def test_habit_initialization():
    """Verifica que un hábito se inicializa con los valores correctos."""
    h = Habit("Leer", "Leer 30 minutos")
    assert h.name == "Leer"
    assert h.description == "Leer 30 minutos"
    assert h.completions == []

def test_add_completion():
    """Verifica que se añade una completitud correctamente."""
    h = Habit("Correr")
    initial_time = datetime.datetime(2025, 1, 1, 9, 30, 0)
    h.add_completion(initial_time)
    assert len(h.completions) == 1
    assert h.completions[0] == initial_time

def test_habit_to_from_dict_conversion():
    """Verifica que el hábito se convierte a diccionario correctamente."""
    original_habit = Habit("Meditar", "10 minutos de meditación")
    original_habit.add_completion(datetime.datetime(2025, 7, 10, 8, 0, 0))
    original_habit.add_completion(datetime.datetime(2025, 7, 11, 8, 0, 0))

    # Convertir a diccionario
    habit_dict = original_habit.to_dict()

    # Recrear desde el diccionario
    recreated_habit = Habit.from_dict(habit_dict)

    assert recreated_habit.name == original_habit.name
    assert recreated_habit.description == original_habit.description
    assert recreated_habit.completions == original_habit.completions