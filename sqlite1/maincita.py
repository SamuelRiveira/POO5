from coleccioncitas import ColeccionCitas
from cita import Cita

cc = ColeccionCitas()
#print(cc.leer())
#cc.buscar(Cita('La vida es bella'))

print(cc.buscar(Cita('La vida es bella')))
print(cc.insertar(Cita('Hola qué tal')))
cc.borrar(Cita('Hola qué tal'))
cc.actualizar("Quedan 2 semanas de clase", "Buenass")
print(cc.leer())