# Desarrolla una aplicación para gestionar una lista circular bidireccional de contactos telefónicos.
# Cada contacto tiene un nombre, un número de teléfono y una dirección de correo electrónico. Se
# debe implementar una lista circular bidireccional para almacenar los contactos. La lista debe
# tener las siguientes funcionalidades. Debe contener las siguientes funciones:
# A. Clases respectivas del problema
# B. Método para agregar un contacto a la lista
# C. Método para mostrar la lista de contactos
# D. Método para buscar un contacto por su nombre
# E. Método eliminar un contacto de la lista
# F. Método para verificar si la lista de contacto está vacía
# Nota: Se solicita no solo implementar las funciones requeridas, sino también probarlas y mostrar los
# resultados obtenidos anteriormente. Esto implica que se deben ejecutar las funciones con datos de
# prueba o ejemplos específicos para demostrar su funcionamiento.

class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo


class Node:
    def __init__(self, contacto):
        self.contacto = contacto
        self.next = None
        self.back = None


class ListaCircularBidireccional:
    def __init__(self):
        self.first = None

    def add(self, contacto):
        newNode = Node(contacto)
        if self.first is None:
            self.first = newNode
            newNode.next = self.first
        else:
            actual = self.first
            while actual.next != self.first:
                actual = actual.next
            actual.next = newNode
            newNode.next = self.first

    def imprimir(self):
        if self.first is None:
            print("La lista está vacía")
        else:
            actual = self.first
            count = 1
            while True:
                print(f"{count}.{actual.contacto.nombre} - Teléfono: {actual.contacto.telefono} - Correo: {actual.contacto.correo}")
                count += 1
                actual = actual.next
                if actual == self.first:
                    break

    def find(self, search):
        if self.first is None:
            print("La lista está vacía")
        else:
            actual = self.first
            while True:
                if actual.contacto.nombre == search:
                    return f"{actual.contacto.nombre} - Teléfono: {actual.contacto.telefono} " \
                           f"- Correo: {actual.contacto.correo}"
                return f'"{search}" no existe'

    def erase(self):
        if self.first is None:
            print("La lista está vacía")
        else:
            actual = self.first
            previo = None
            search = input("Ingrese el nombre del contacto que desea borrar: ")
            if actual.contacto.nombre == search:
                print(f'El contacto "{search}" fue borrado exitosamente')
                while True:
                    if actual.contacto.nombre == search:
                        if previo is not None:
                            previo.next = actual.next
                        else:
                            while actual.next != self.first:
                                actual = actual.next
                            actual.next = self.first.next
                            self.first = self.first.next
                        return
                    elif actual.next == self.first:
                        return
                    previo = actual.back
                    actual = actual
            else: print(f'El contacto "{search}" no se encuentra en la lista')





contacts = ListaCircularBidireccional()
contacts.imprimir()
# al no haber nada debe mostrar "La lista está vacía"
contacts.erase()
# al no haber nada debe mostrar "La lista está vacía"
print()
contacts.add(Contacto("Antoine", "+569 3610 2983", "muertexer@gmail.com"))
contacts.add(Contacto("Felipe", "+569 8764 6513", "algo2@gmail.com"))
contacts.imprimir()
# Entrega:
# 1.Antoine - Teléfono: +569 3610 2983 - Correo: muertexer@gmail.com
# 2.Felipe - Teléfono: +569 8764 6513 - Correo: algo2@gmail.com

print()
print(contacts.find("Antoine"))
# debe entregar: Antoine - Teléfono: +569 3610 2983 - Correo: muertexer@gmail.com
print()
contacts.erase()
# borra la lista Antoine
print()
contacts.imprimir()
# debe solo imprimir
# 1.Felipe - Teléfono: +569 8764 6513 - Correo: algo2@gmail.com




