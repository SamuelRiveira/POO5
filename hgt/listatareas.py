from tarea import Tarea
class ListaTareas:

    limitador = "|##|"

    def __init__(self, listaTareas:list):
        listaTareas = []
        self.listaTareas = listaTareas

    def agregar(self, tarea:Tarea):
        self.listaTareas.append(tarea)

    def leer(self):
        resultado = ""
        for tarea in self.listaTareas:
            resultado += tarea
            if tarea != self.listaTareas[-1]:
                resultado += self.limitador
        
        return resultado
    
    def cargar(self, data:str):
        tareas = data.split(self.limitador)
        for tarea in tareas:
            self.listaTareas.append(tarea)

    def actualizar(self, tarea:Tarea, estado:bool):
        for elemento in self.listaTareas:
            if elemento == tarea:
                elemento.actualizar(estado)
                break

    def eliminar(self, tarea:Tarea):
        for elemento in self.listaTareas:
            if elemento == tarea:
                elemento.eliminar()
                break

    def __str__(self):
        return self.leer()
    
    def __len__(self):
        return self.listaTareas.__len__()
    
    def __getitem__(self, indice):
        return self.listaTareas[indice]
    
    def __setitem__(self, indice, valor):
        self.listaTareas[indice] = valor

    def __delitem__(self, indice):
        del self.listaTareas[indice]

    def __iter__(self):
        return self.listaTareas.__iter__()
    
    def __next__(self):
        return self.listaTareas.__next__()
    
    def __contains__(self, item):
        return item in self.listaTareas
    
    def __eq__(self, other):
        return self.listaTareas == other.listaTareas
    
    def __ne__(self, other):
        return self.listaTareas != other.listaTareas