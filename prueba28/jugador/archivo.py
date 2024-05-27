class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre

    def leer(self):
        try:
            f = open(self.nombre, 'rt')
        except FileNotFoundError:
            return ""
        with f:
            return f.readline()

    def escribir(self, texto):
        try:
            f = open(self.nombre, 'wt')
        except:
            raise Exception("Error")

            with f:
                f.write(texto)
                return true