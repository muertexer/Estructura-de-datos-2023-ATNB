# este codigo es netamente para hacer practicas antes de ser agregado al codigo oficial (los ejercicios)


''''''
'''
result_list = []
for i in range(10):
    result_list.append(hash(i) % 10+1)
print(result_list)

result_list = []
for i in range(10):
    result_list.append(id(i) % 5+1)
print(result_list)

import random
result_list = []
for i in range(10):
    result_list.append(random.randint(1,5))
print(result_list)

m = []
for i in range(2):
    filas = []
    for j in range(2):
        rndi = ((id(i) + id(j)) % 5) + 1
        filas.append(rndi)
    m.append(filas)
print(m)
'''

def generar_matriz_aleatoria(semilla=None):
    if semilla is None:
        semilla = "semilla_predeterminada"
    matriz = [[hash(f"{i},{j},{semilla}") % 5 + 1 for j in range(2)] for i in range(2)]
    return matriz

matriz_aleatoria_1 = generar_matriz_aleatoria("semilla_1")
print(matriz_aleatoria_1)

matriz_aleatoria_2 = generar_matriz_aleatoria("semilla_2")
print(matriz_aleatoria_2)