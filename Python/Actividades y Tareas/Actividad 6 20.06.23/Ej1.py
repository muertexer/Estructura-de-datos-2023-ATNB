# EJERCICIO DE LISTA ENLAZADA
# Realizar un algoritmo que permita simular una lista enlazada que permita agregar frutas. Se
# debe crear un menú que llame las siguientes funciones:
# A) Agregar un fruta al final de la lista
# B) Agregar una fruta al inicio
# C) Eliminar una fruta
# D) Imprimir la lista actual
# E) Obtener cabecera
# F) Obtener cola


# APUNTES CLASE:

# EJERCICIO DE COLA
# Realizar un algoritmo que permita simular el proceso de atención en un banco. Se debe crear
# una lista con los nombres de los clientes. Utilizar clases y funciones.

class Node():
    dato = None
    siguiente = None
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

def addToEnd(firstNode, dato):
    newNode = Node(dato)
    if firstNode is None:
        firstNode = newNode
        return firstNode
    temp = firstNode
    while temp.siguiente:
        temp = temp.siguiente
    temp.siguiente = newNode
    return firstNode

def addToStart(firstNode, dato):
    newNode = Node(dato)
    newNode.siguiente = firstNode
    return newNode

def printList(node):




