# 4. Desarrollar un algoritmo que contenga seis productos de supermercado utilizando colas
# con Python, implementando las siguientes funciones:
# a) Hacer un metodo que agregue un producto a la cola. ´
# b) Crear otro metodo para eliminar el primer producto de la cola. ´
# c) Otra funcion que muestre los productos en la cola sin modificar la cola, utilizando ´
# ciclos.
# d) Un metodo que invierta el orden de productos de la cola. ´
# e) Una funcion que elimine todos los productos de la cola.

class Cola:
    def __init__(self):
        self.items = ["Pilas", "Aceite", "Sal", "Arroz", "Harina", "Fideos"]
    def add(self, x):
        self.items.append(x)
    def remove(self):
        if self.empty():
            raise ValueError("La cola está vacia")
        return self.items.pop(0)
    def show(self):
        lista = ""
        count = 1
        for item in self.items:
            lista += f"{count}. {str(item)}\n"
            count += 1
        return lista
    def empty(self):
        return len(self.items) == 0
    def invert(self):
        return self.items.reverse()
    def clear(self):
        self.items.clear()
        return str(self.items)


sup = Cola()
print(f"La cola original es: \n{sup.show()}")

sup.remove()
print(f"La cola sin el primer elemento es: \n{sup.show()}")

sup.invert()
print(f"La cola invertida es: \n{sup.show()}")

print(f"La cola con sus elementos eliminados es: \n{sup.clear()}")



