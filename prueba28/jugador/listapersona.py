from persona import Persona

class ListaPersona:
    limitador = ','

    def __init__(self):
        self.personas = []

    def add(self, persona: Persona):
        self.personas.append(persona)

    def read(self) -> str:
        resultado = ""
        for persona in self.personas:
            resultado += persona.read()
            if persona != self.personas[-1]:
                resultado += self.limitador
        return resultado

    def load(self, data: str):
        nombres = data.split(self.limitador)
        for nombre in nombres:
            persona = Persona(nombre)
            self.personas.append(persona)

    def update(self, nombre_actual: str, nombre_nuevo: str):
        for p in self.personas:
            if p.read() == nombre_actual:
                p.update(nombre_nuevo)
                break

    def delete(self, nombre: str):
        for p in self.personas:
            if p.read() == nombre:
                p.delete()
                break
