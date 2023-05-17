# Crear un algoritmo donde se solicite dos matrices por consola.
# Tanto la cantidad de columnas como de filas, deben ser ingresadas por teclado.
# Los elementos de las matrices deben ser generados de forma aleatoria (0 al 5).
# Estas dos matrices se deben sumar.
# Luego se solicita una tercera matriz.
# Al igual que las dos anteriores, se ingresan columnas y filas por consola,
# y sus elementos son generados aleatoriamente (0 a 5).
# Esta última matriz se restará con la matriz resultante entre la operación de suma.

# Por Antoine Briones y Cristopher González

print("Creación de tres matrices")
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
print(f"\nSuma matrices (1+2): ")
for fila in mfinal:
    print(fila)

m3 = crearMtrx(filas,columnas, "algo3")
print(f"\nMatriz 3:")
for fila in m3:
    print(fila)

mfinal = restaMtrx(mfinal, m3)
print(f"\nResta matrices (1+2-3): ")
for fila in mfinal:
    print(fila)
