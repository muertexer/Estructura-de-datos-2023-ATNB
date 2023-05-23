# Crear dos matrices donde la cantidad de filas y columnas serán 3 x 3. Los
# elementos de estas matrices deben ser generados de forma aleatoria (-5 a -10).
# Luego se deben multiplicar ambas matrices e imprimir la matriz resultante.
# Agregar una condición para que las dimensiones sean acordes para realizar la
# multiplicación entre ambas matrices.
# Esta matriz resultado se debe multiplicar por una matriz identidad, e imprimir la matriz final.
# Se pueden utilizar librerías para resolver todo el ejercicio.

import numpy as np

# Matriz 1
f1 = 3
c1 = 3
m1 = np.random.randint(-10, -4, (f1, c1))
print("Matriz 1:")
print(m1)

# Matriz 2
f2 = 3
c2 = 3
m2 = np.random.randint(-10, -4, (f2, c2))
print("\nMatriz 2:")
print(m2)

# m1 * m2
mMult = np.matmul(m1,m2)
if f1 == c2:
    print("\nProducto de matrices:")
    for a in mMult:
        print(a)
else: print("Las dimensiones no son acordes para realizar la multiplicación")

# Innecesario, pero es netamente para que sea comparable
c3 = 3
I = np.identity(c3)
print("\nMatriz Identidad (3x3):")
for f in I:
    print(f)

if  f2 == c3:
    mMultIde = np.matmul(mMult,I)
    print("\nProducto final por matriz identidad:")
    for a in mMultIde:
        print(a)
else:
    print("Las dimensiones no son acordes para realizar la multiplicación")