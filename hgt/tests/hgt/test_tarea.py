import pytest

from tarea import Tarea

@pytest.fixture
def tarea():
    return Tarea('Tarea1')

def test_tarea(tarea):
    assert tarea.leer() == 'Tarea1'

def test_leer(tarea):
    assert tarea.leer() == 'Tarea1'

def test_actualizar(tarea):
    tarea.actualizar('Tarea2')
    assert tarea.leer() == 'Tarea2'

def test_eliminar(tarea):
    tarea.eliminar()
    assert tarea.leer() == None