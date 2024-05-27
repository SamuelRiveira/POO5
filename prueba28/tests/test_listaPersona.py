from listapersona import ListaPersona
from archivo import Archivo
import pytest
import os

FILENAME = 'lista_personas.dat'
DATA = 'Juan,Pedro'

@pytest.fixture
def archivo():
    return Archivo(FILENAME)

def test_archivoLeer(archivo):
    # Eliminar el archivo si existe
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
    assert archivo.leer() == ''

def test_archivoEscribir(archivo):
    assert archivo.escribir(DATA) == True

def test_archivoLeer2(archivo):
    assert archivo.leer() == DATA

def test_archivoListaPersona(archivo):
    lista = ListaPersona()
    lista.load(archivo.leer())
    assert lista.read() == DATA

def test_listaPersonaUpdate(archivo):
    lista = ListaPersona()
    lista.load(archivo.leer())
    lista.update('Pedro', 'Pablo')
    assert 'Pablo' in lista.read()
    assert 'Pedro' not in lista.read()

def test_listaPersonaDelete(archivo):
    lista = ListaPersona()
    lista.load(archivo.leer())
    lista.delete('Juan')
    assert 'Juan' not in lista.read()
