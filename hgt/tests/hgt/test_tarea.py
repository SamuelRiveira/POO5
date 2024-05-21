import pytest

from tarea import Tarea

@pytest.fixture
def tarea():
    return Tarea(1, 'Tarea1', False)

def test_tarea(tarea):
    assert tarea.leer() == f"ID: {tarea.id}\nTarea: {tarea.tarea}\nEstado: {tarea.estado}"

def test_leer(tarea):
    assert tarea.leer() == f"ID: {tarea.id}\nTarea: {tarea.tarea}\nEstado: {tarea.estado}"

def test_actualizar(tarea):
    tarea.actualizar('Tarea2', True)
    assert tarea.leer() == f"ID: {tarea.id}\nTarea: {tarea.tarea}\nEstado: {tarea.estado}"

def test_eliminar(tarea):
    tarea.eliminar()
    assert tarea.leer() == f'ID: None\nTarea: None\nEstado: None'