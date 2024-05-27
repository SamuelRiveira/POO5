from listajugador import ListaJugador
from archivo import Archivo
import pytest
import os

FILENAME = 'lista.dat'
DATA = 'Juan, futbol' + ListaJugador.limitador + 'Pedro, baloncesto'

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

def test_archivoListaJugador(archivo):
    lista = ListaJugador()
    lista.load(archivo.leer())
    assert lista.read() == DATA