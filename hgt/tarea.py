class Tarea:
    def __init__(self, id:int, tarea:str, estado:bool) -> None:
        self.id     = id
        self.tarea  = tarea
        self.estado = estado

    #Métodos CRUD
    def leer(self) -> str:
        return f"ID: {self.id}\nTarea: {self.tarea}\nEstado: {self.estado}"

    def actualizar(self, tarea, estado) -> None:
        self.tarea = tarea
        self.estado = estado

    def eliminar(self):
        self.tarea = None
        self.id = None
        self.estado = None