# Crear dos matrices solicitando la cantidad de filas y columnas por teclado.
# Los elementos deben ser enteros generados de manera aleatoria (números del 1 al 5).
# Luego se deben sumar estas matrices, solamente utilizando elementos propios de Python (no se permite uso de librerías).
# Imprimir la matriz resultante de la suma.
# La matriz resultante de la suma anterior se debe multiplicar por un escalar entero (del 1 al 10) ingresado por teclado.
# En este caso, sí se puede utilizar la librería numpy.
# Imprimir la matriz resultante entre esta operación.
# Por último al obtener la matriz resultante del paso anterior, esta se debe multiplicar por una nueva matriz,
# la que debe tener las dimensiones acordes para realizar la multiplicación entre ambas matrices.
# Esta matriz se debe ingresar por teclado tanto la cantidad de filas y columnas como sus elementos.
# Se permite el uso de la librería numpy. Imprimir la matriz final obtenida.

# filas = int(input("Ingrese la cantidad de filas para la matriz: "))
# columnas = int(input("Ingrese la cantidad de columnas para la matriz: "))

def crearMTRX(fil, col, semilla = None):
    for i in range(fil):
        fila = []
        for j in range(col):
            rnd = hash(semilla) % 5 + 1
            fila.append(rnd)
        return fila

def sumMTRX(m , m2):
    mf = []
    for i in range(m):
        for j in range(m2):
            mf = m+m2
        return mf[i][j]


a = crearMTRX(5,5,"algo")
print("matriz 1:")
for i in a:
    print(a)
print("matriz 2:")
a2 = crearMTRX(1,5,"algo")
for i in a2:
    print(i)

"""print("suma matrices:")
mf = sumMTRX(a, a2)
for i in mf:
    print(i)
"""

import numpy

mult = int(input("Ingrese un numero entero del 1 al 10 para multiplicar la matriz resultante: "))
if 1 < mult < 10:
    numpy.multiply(mf, mult)
else: print("Ingrese un valor entre 1 y 10")

filas3 = int(input("Ingrese la cantidad de filas para la matriz, "
                   "estas deben ser iguales a la cantidad de columnas ingresadas anteriormente: "))
columna3 = int(input("Ingrese la cantidad de columnas para la matriz: "))

m3 = []
for i in range(filas3):
    fila = []
    for j in range(columna3):
        m3[i][j] = input(f"Ingrese el elemento {i} y el elemento {j}")

# faltó arreglar la creacion de la matriz con el hash, corregir la suma de las matrices
# y revisar la creacion de la ultima matriz