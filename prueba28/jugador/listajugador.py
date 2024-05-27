from jugador import Jugador

class ListaJugador:
    limitador = ','

    def __init__(self):
        self.jugadores = []

    def add(self, jugador: Jugador):
        self.jugadores.append(jugador)

    def read(self) -> str:
        resultado = ""
        for jugador in self.jugadores:
            resultado += jugador.read()
            if jugador != self.jugadores[-1]:
                resultado += self.limitador
        return resultado

    def load(self, data: str):
        jugadores = data.split(self.limitador)
        for jugador_str in jugadores:
            nombre, deporte = jugador_str.split(', ')
            jugador = Jugador(nombre, deporte)
            self.jugadores.append(jugador)

    def update(self, nombre, deporte):
        for j in self.jugadores:
            if j.deporte == deporte and j.nombre == nombre:
                j.update(nombre, deporte)
                break

    def delete(self, nombre, deporte):
        for j in self.jugadores:
            if j.deporte == deporte and j.nombre == nombre:
                j.delete()
                break
