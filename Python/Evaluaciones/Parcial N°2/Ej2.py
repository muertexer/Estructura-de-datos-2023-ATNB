# Desarrolla un sistema de gestión de inventario utilizando listas bidireccionales. Cada artículo del
# inventario tiene un código único, un nombre, una descripción y una cantidad disponible. El
# sistema debe realizar las siguientes operaciones:
# A. Agregar un artículo al inventario, ingresando su código, nombre, descripción y cantidad
# inicial
# B. Eliminar un artículo del inventario utilizando su código
# C. Buscar un artículo en específico por su código
# D. Actualizar la cantidad disponible de un artículo
# E. Mostrar todos los artículos del inventario en orden ascendente según su código
# Nota: Se solicita no solo implementar las funciones requeridas, sino también probarlas y mostrar los
# resultados obtenidos anteriormente. Esto implica que se deben ejecutar las funciones con datos de
# prueba o ejemplos específicos para demostrar su funcionamiento.



class Articulo:
    def __init__(self, codigo, nombre, cantidad, descripcion):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.descripcion = descripcion



class Node:
    def __init__(self, articulo):
        self.articulo = articulo
        self.last = None
        self.next = None
        self.back = None


class ListaBiDireccional:
    def __init__(self):
        self.first = None
        self.last = None

    def addFirst(self, articulo):
        newNode = Node(articulo)
        if self.first is None:
            self.first = newNode
            self.last = newNode
        else:
            newNode.next = self.first
            self.first.back = newNode
            self.first = newNode

    def addLast(self, articulo):
        newNode = Node(articulo)
        if self.first is None:
            self.first = newNode
            self.last = newNode
        else:
            newNode.back = self.last
            self.last.next = newNode
            self.last = newNode

    def erase(self):
        if self.first is None:
            return "La lista está vacía"
        else:
            search = input("Ingrese el código del artículo que desea borrar: ")
            actual = self.first
        while actual:
            if actual.articulo.codigo == search:
                if actual.back:
                    actual.back.next = actual.next
                else: self.first = actual.next
                if actual.next:
                    actual.next.back = actual.back
                else: self.last = actual.back
                break
            actual = actual.next

    def find(self, search):
        actual = self.first
        while actual:
            if actual.articulo.codigo == search:
                return f"Código: {actual.articulo.codigo} - Nombre: {actual.articulo.nombre} ({actual.articulo.cantidad}) - Descripción: {actual.articulo.descripcion}"
            actual = actual.next
        return f"El Código {search} no existe"

    def changeQuantity(self):
        if self.first is None:
            print("La lista está vacía")
        else:
            search = input("Ingrese el código del artículo que desea modificar: ")
            actual = self.first
            while actual:
                if actual.articulo.codigo == search:
                    cant = int(input("Ingrese la cantidad disponible de artículos: "))
                    actual.articulo.cantidad = cant
                actual = actual.next
            return "El código no se encuentra en la lista de artículos"

    def imprimir(self):
        if self.first is None:
            print("La lista está vacía")
        else:
            articulos = []
            actual = self.first
            while actual is not None:
                articulos.append(actual.articulo)
                actual = actual.next

            ordered = sorted(articulos, key=lambda articulo: articulo.codigo)

            for articulo in ordered:
                print(f"Código: {articulo.codigo} - Nombre: {articulo.nombre} ({articulo.cantidad}) "
                      f"- Descripción: {articulo.descripcion}")


lista = ListaBiDireccional()
lista.imprimir()
lista.addFirst(Articulo(2, "Serranitas", "2", "GAlletas"))
lista.imprimir()
print()
lista.addFirst(Articulo(23, "Serranitassss", "2323", "GAlletas"))
lista.imprimir()
print("BUSQUEDA")
print(lista.find(2))


