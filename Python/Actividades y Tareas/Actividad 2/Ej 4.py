# Crear un arreglo aleatorio de tamaño entre 10 a 30 [10;30]
# Imprimir el arreglo creado y luego solicitar por consola
# la busqueda de un elemento en especifico del arreglo creado.
# Todo esto utilizando array

A = [chr(hash("semilla" + str(i)) % 26 + 97) for i in range(hash("semilla") % 21 + 10)]

Search = input(f'En "{"".join(A)}"\n¿Qué elemento desea buscar? ')
indices = []
for i in range(len(A)):
    if A[i] == Search:
        indices.append(i+1)
if Search in A:
    print(f'El elemento "{Search}" está presente en la posición {indices} del arreglo.')
else:
    print(f'El elemento "{Search}" no está presente en el arreglo.')