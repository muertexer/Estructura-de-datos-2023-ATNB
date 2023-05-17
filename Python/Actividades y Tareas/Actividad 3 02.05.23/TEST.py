"""
# Crear la primera matriz de 2x3 con valores al azar
matriz1 = [[2, 3, 1], [4, 2, 5]]

# Crear la segunda matriz de 3x2 con valores al azar
matriz2 = [[1, 4], [2, 3], [3, 2]]

# Crear una matriz de ceros de tamaño 2x2 para almacenar el resultado
resultado = [[0, 0], [0, 0]]

# Multiplicar las dos matrices
for i in range(len(matriz1)):
    for j in range(len(matriz2)):
        for k in range(len(matriz2)):
            resultado[i][j] += matriz1[i][k] * matriz2[k][j]

# Imprimir el resultado de la multiplicación
print("Resultado de la multiplicación:")
for fila in resultado:
    print(fila)
"""

def transpose_matrix(matrix):
    # Obtener el número de filas y columnas de la matriz
    rows, cols = len(matrix), len(matrix[0])
    # Crear una nueva matriz con las filas y columnas invertidas
    transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    return transposed_matrix


# Crear una matriz de ejemplo
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Transponer la matriz
transposed_matrix = transpose_matrix(matrix)

# Imprimir la matriz original y la transpuesta
print("Matriz original:")
for row in matrix:
    print(row)

print("Matriz transpuesta:")
for row in transposed_matrix:
    print(row)