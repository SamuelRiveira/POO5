import pytest

from jugador import Jugador

@pytest.fixture
def jugador():
    return Jugador("William", "Cricket")

def test_read(jugador):
    assert jugador.read() == "William, Cricket"