# test_archivo.py

import pytest
import os
from archivo import Archivo

@pytest.fixture
def archivo():
    nombre_archivo = "testfile.txt"
    archivo = Archivo(nombre_archivo)
    yield archivo
    try:
        os.remove(nombre_archivo)
    except FileNotFoundError:
        pass

def test_create_archivo(archivo):
    texto = "Hola, mundo!"
    archivo.escribir(texto)
    assert archivo.leer() == texto

def test_update_archivo(archivo):
    texto = "Nuevo contenido"
    archivo.escribir(texto)
    assert archivo.leer() == texto

def test_delete_archivo(archivo):
    archivo.escribir("Contenido temporal")
    os.remove(archivo.nombre)
    assert archivo.leer() == ""
