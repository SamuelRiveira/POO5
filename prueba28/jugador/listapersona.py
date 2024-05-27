from persona import Persona

class ListaPersona:

    limitador = []

    def __init__(self):
        self.personas = []

    def add(self, persona:Persona):
        self.personas.append(persona)

    def read(self):
        resultado = ""
        for persona in self.personas:
            resultado += persona
            if persona != self.personas[-1]:
                resultado += self.limitador
        return resultado

    def load(self, data:str):
        personas = data.split(self.limitador)
        for persona in personas:
            self.personas.append(persona)

    def update(self, persona:Persona, nombre):
        for p in self.personas:
            if p == persona:
                p.update(nombre)
                break
    
    def delete(self, persona:Persona):
        for p in self.personas:
            if p == persona:
                p.delete()
                break