# Obtener la determinante de una matriz de 3 x 3 con sus elementos aleatorios (5 al 10, enteros positivos).
# Se pueden utilizar librerías para resolver el algoritmo.
import numpy as np

m = np.random.randint(5, 11, (3, 3))
print("Matriz:")
print(m)

det = np.linalg.det(m)
print(f"Determinante: {det}")
