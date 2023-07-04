# EJERCICIO DE PILA
# Realizar un algoritmo que permita simular el proceso de apilar libros en una biblioteca, y
# luego ir sacándolos utilizando el principio de pilas. Utilizar clases y funciones.

# pila
class stack:
    def __init__(self):
        self.top = None
        self.stack = [str(input("Ingrese un libro: "))]
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


algo = stack()
algo.push(1)
algo.push(3)
algo.push(4)
algo.push(7)
print(algo)

algo.pop()
print(algo)
print(algo.size())

