import pytest

from persona import Persona

@pytest.fixture
def persona():
    return Persona("William")

def test_create_persona():
    assert presona.read == "William"

