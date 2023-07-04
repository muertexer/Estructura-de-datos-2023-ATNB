# EJERCICIO DE COLA
# Realizar un algoritmo que permita simular el proceso de atención en un banco. Se debe crear
# una lista con los nombres de los clientes. Utilizar clases y funciones.

#cola
class Cola:
    def __init__(self):
        self.items = []
    def encolar(self, x):
        self.items.append(x)
    def desencolar(self):
        if self.empty():
            raise ValueError("La cola está vacia")
        return self.items.pop(0)
    def empty(self):
        return len(self.items) == 0
    def __str__(self):
        return str(self.items)

cola = Cola()
cola.encolar("AJSGDASHD")
cola.encolar(2)
cola.encolar(3)
print(cola)
cola.desencolar()
print(cola)