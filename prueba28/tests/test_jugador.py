import pytest

from jugador import Jugador

@pytest.fixture
def jugador():
    return Jugador("William", "Cricket")

def test_create_jugador():
    assert jugador.read() == "William, Cricket"

def test_update_jugador():
    jugador.update("John", "Football")
    assert jugador.update() == "John, Football"

def test_delete_jugador():
    jugador.delete()
    assert jugador.delete() == None