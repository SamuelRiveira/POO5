import pytest

from persona import Persona

@pytest.fixture
def persona():
    return Persona("William")

def test_create_persona():
    assert presona.read == "William"

def test_update_persona():
    persona.update("John")
    assert persona.read == "John"

def test_delete_persona():
    persona.delete()
    assert persona.read == None
