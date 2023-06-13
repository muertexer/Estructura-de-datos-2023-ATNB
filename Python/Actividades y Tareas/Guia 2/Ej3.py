# 3. Realizar un algoritmo utilizando la estructura de Pila en Python. Se desea almacenar el
# siguiente conjunto de documentos:
# documentos = [“Informe Final”, “Guia de Estudio”, “Tesis 4”, “Seminario Osorno”]
# a) Crear una funcion e imprimir el listado de documentos actual de la pila. ´
# b) Agregar el documento “Avance Tesis” y “Proyecto Integrador”.
# c) Obtener el ultimo elemento superior de la pila. ´
# d) Eliminar el documento de la parte superior.
# e) Imprimir la pila de documentos actualizadas.
# f) Verificar si esta vac´ıa la pila de documentos.

class stack:
    def __init__(self):
        self.top = None
        self.stack = ["Informe Final", "Guia de Estudio", "Tesis 4", "Seminario Osorno"]
    def push(self,item):
        self.top = item
        self.stack.append(item)
        return self.top
    def pop(self):
        if not self.is_empty():
            self.stack.pop()
            self.top = self.stack[-1]
            return self.top
        else:
            raise IndexError("El stack está vacio")
    def __str__(self):
        return str(self.stack)
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)


Documentos = stack()
print(f"La pila original es: {Documentos.__str__()}")

Documentos.push("Avance Tesis"), Documentos.push("Proyecto Integrador")
print(f'\nLa pila agregando los documentos "Avance Tesis" y "Proyecto Integrador" es: \n{Documentos.__str__()}')

print(f"\nEl ultimo elemento superior de la pila es: {Documentos.top}")

Documentos.pop()
print(f"\nLa pila eliminando el documento de la parte superior quedaria como: \n{Documentos.__str__()}")

print(f"\n¿La pila se encuentra vacia?    R: {Documentos.is_empty()}")


