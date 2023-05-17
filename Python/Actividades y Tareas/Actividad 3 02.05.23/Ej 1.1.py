# USANDO NUMPY, multiplicacion de dos matrices y crear su traspuesta
import numpy

print("Creación de matriz 1")
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

m = numpy.zeros((filas, columnas))
for i in range(filas):
    filas = []
    for j in range(columnas):
        m[i][j] = int(input(f"Elemento ({i + 1}, {j + 1}): "))


print("\nCreación de matriz 2")
filas2 = int(input("Ingrese la cantidad de filas: "))
columnas2 = int(input("Ingrese la cantidad de columnas: "))

m2 = numpy.zeros((filas2, columnas2))
for i in range(filas2):
    filas2 = []
    for j in range(columnas2):
        m2[i][j] = int(input(f"Elemento ({i + 1}, {j + 1}): "))

#Para multiplicar matrices usar:
# m @ m2 O numpy.matmul(m,m2)

mfinal = m @ m2
print("La matriz resultante es: ")
for fila in mfinal:
    print(fila)
print(f"Las dimensiones de la matriz son \n{numpy.shape(mfinal)}")

mtraspuesta = numpy.transpose(mfinal)
print("La matriz resultante es: ")
for fila in mtraspuesta:
    print(fila)
print(f"Las dimensiones de la matriz son \n{numpy.shape(mtraspuesta)}")


