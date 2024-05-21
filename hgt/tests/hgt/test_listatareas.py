from listatareas import ListaTareas
import pytest

@pytest.fixture
def lista():
    return ListaTareas()

# Test de la clase ListaTareas
def test_listaTareas0(lista):
    assert len(lista) == 0

def test_listaTareas1(lista):
    lista.agregar('Tarea1')
    assert len(lista) == 1

def test_listaTarea2(lista):
    lista.agregar('Tarea1')
    lista.agregar('Tarea2')

    assert len(lista) == 2

    assert lista[0] == 'Tarea1'
    assert lista[1] == 'Tarea2'

def test_listaTareaEliminar(lista):
    lista.agregar('Tarea3')
    assert lista[0] == 'Tarea3'

    del lista[0]
    assert len(lista) == 0

    assert 'Tarea3' not in lista

def test_listaLeer(lista):
    lista.agregar('Tarea1')
    lista.agregar('Tarea2')

    assert lista.leer() == 'Tarea1' + lista.limitador + 'Tarea2'

def test_listaCargar(lista):
    lista.cargar('Tarea1' + lista.limitador + 'Tarea2')
    assert len(lista) == 2

    assert lista[0] == 'Tarea1'
    assert lista[1] == 'Tarea2'
