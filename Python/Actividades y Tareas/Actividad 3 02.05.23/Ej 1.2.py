# SIN USAR NUMPY, multiplicacion de dos matrices y crear su traspuesta


def crearMtrx(filas, columnas, seed=None):
    a = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            if seed is None:
                seed = "standard"
            rnd1 = (hash(f"{i},{j},{seed}") % 5+1)
            fila.append(rnd1)
        a.append(fila)
    return a



print("Creación de matriz 1")
columnas = int(input("Ingrese la cantidad de columnas: "))
filas = int(input("Ingrese la cantidad de filas: "))

m = crearMtrx(filas,columnas, "algo1")
print(f"\nMatriz 1:")
for fila in m:
    print(fila)

print("\nCreación de matriz 2")
columnas2 = int(input("Ingrese la cantidad de columnas: "))
filas2 = int(input("Ingrese la cantidad de filas: "))

m2 = crearMtrx(columnas,filas2, "algo2")
print(f"\nMatriz 2:")
for fila in m2:
    print(fila)

#Matriz final para calculos
mf = []
for i in range(filas2):
    fila = []
    for j in range(columnas):
        rnd1 = 0
        fila.append(rnd1)
    mf.append(fila)

# Multiplicación
if filas == columnas2:
    for i in range(0,len(m)):
        fila = []
        for j in range(0,len(m2)):
            mf[i][j] = m[j][i] * m2[i][j]
        fila.append(mf)
    print(f"\nMultiplicacón de matrices: ")
    for fila in mf:
        print(fila)
else:
    print("No se puede realizar la operacion ya que la cantidad de filas en la matriz 1 no es igual a "
          "la cantidad de columnas en la matriz 2")



# Traspuesta

filas, columnas = len(mf), len(mf[0])

# Traspuesta manera 1
tras = [[mf[j][i] for j in range(filas)] for i in range(columnas)]

print("\nMatriz transpuesta 1.0:")
for row in tras:
    print(row)

# Traspuesta manera 2.0

tras = []
for j in range(columnas):
    fila = []
    for i in range(filas):
        fila.append(mf[i][j])
    tras.append(fila)

print("\nMatriz transpuesta 2.0:")
for row in tras:
    print(row)