# Crear una matriz la cual se debe solicitar por teclado la cantidad de filas y columnas que va a contener.
# También ingresar por consola un escalar.
# Los elementos de la matriz deben ser generados aleatoriamente (0 al 10).
# Por último, se debe multiplicar la matriz generada por el escalar ingresado.

# Por Antoine Briones y Cristopher González

print("Creación de una matriz")
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

def crearMtrx(filas, columnas, seed=None):
    a = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            if seed is None:
                seed = "standard"
            rnd1 = (hash(f"{i},{j},{seed}") % 11)
            fila.append(rnd1)
        a.append(fila)
    return a

def multMtrx(m,n):
    mf = []
    for i in range(len(m)):
        fila = []
        for j in range(len(m[0])):
            mult = m[i][j] * n
            fila.append(mult)
        mf.append(fila)
    return mf

m = crearMtrx(filas,columnas, "algo1")
print(f"\nMatriz:")
for fila in m:
    print(fila)

n = int(input("\nIngrese un escalar con el cual multiplicar la matriz: "))

mfinal = multMtrx(m, n)
print(f'\nMultiplicación de matriz por el escalar "{n}": ')
for fila in mfinal:
    print(fila)