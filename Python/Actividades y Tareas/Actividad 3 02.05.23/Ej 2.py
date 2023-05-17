# Comprobar (A + B)^T = A^T + B^T

print("Creación de dos matrices")
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))
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


def sumaMtrx(m,m2):
    mf = []
    for i in range(len(m)):
        fila = []
        for j in range(len(m[0])):
            suma = m[i][j] + m2[i][j]
            fila.append(suma)
        mf.append(fila)
    return mf


m = crearMtrx(filas,columnas, "algo1")
print(f"\nMatriz 1:")
for fila in m:
    print(fila)

m2 = crearMtrx(filas,columnas, "algo2")
print(f"\nMatriz 2:")
for fila in m2:
    print(fila)

mfinal = sumaMtrx(m, m2)
print(f"\nSuma matrices: ")
for fila in mfinal:
    print(fila)

# Traspuesta (A+B)^T
filas, columnas = len(mfinal), len(mfinal[0])
tras = [[mfinal[j][i] for j in range(filas)] for i in range(columnas)]

print("\nMatriz transpuesta forma (A+B)^T:")
for fila in tras:
    print(fila)

# Traspuesta A^T + B^T
print("\nTraspuesta A^T + B^T")

filas, columnas = len(m), len(m[0])
tras1 = [[m[j][i] for j in range(filas)] for i in range(columnas)]

filas, columnas = len(m2), len(m2[0])
tras2 = [[m2[j][i] for j in range(filas)] for i in range(columnas)]

mfinal = sumaMtrx(tras1, tras2)
print(f"Suma matrices: ")
for fila in mfinal:
    print(fila)

if tras == mfinal: print("\nSi se cumple que (A + B)^T = A^T + B^T")
else: print("\nNo se cumple que (A + B)^T = A^T + B^T")

