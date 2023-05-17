# Crear dos matrices solicitando los datos por consola (cantidad de filas y columnas), y los
# elementos de estas matrices deben ser aleatorios del 1 al 5, no se deben ingresar por
# consola. Luego se deben sumar en una función las matrices, y en otra función restarlas. En
# este caso no se puede utilizar numpy, solo estructuras propias de Python.

# FINALIZADO Y CORREGIDO 25/04
# ORIGINIAL HECHO EL 18/04


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

def restaMtrx(m,m2):
    mf = []
    for i in range(len(m)):
        fila = []
        for j in range(len(m[0])):
            res = m[i][j] - m2[i][j]
            fila.append(res)
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

mfinal = restaMtrx(m, m2)
print(f"\nResta matrices: ")
for fila in mfinal:
    print(fila)

