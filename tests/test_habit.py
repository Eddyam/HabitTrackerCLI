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

