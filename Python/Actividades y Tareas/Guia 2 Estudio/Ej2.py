# 2. Se tiene una tupla con las siguientes frutas:
# frutas = (“manzana”, “platano”, “pera”, “naranja”, “frutilla”, “manzana”) ´
# Realizar las siguientes operaciones:
# a) Eliminar los elementos repetidos de la tupla.
# b) Agregar la fruta “mango” por teclado.
# c) Eliminar la fruta platano. ´
# d) Calcular la cantidad de frutas que existen.


frutas = ("manzana", "platano", "pera", "naranja", "frutilla", "manzana")
imp = ", ".join(str(algo) for algo in frutas)
print(f"La tupla original es: {imp}")

frutas = tuple(set(frutas))
imp = ", ".join(str(algo) for algo in frutas)
print(f'\nLa tupla sin los elementos repetidos es: {imp}')

x = input("\nIngrese un elemento a agregar: ")
frutas = frutas + (x,)
imp = ", ".join(str(algo) for algo in frutas)
print(f"\nLa tupla con el elemento agregado es: {imp}")

y = "platano"
frutas = tuple(z for z in frutas if z != y)
imp = ", ".join(str(algo) for algo in frutas)
print(f'\nLa tupla sin el elemento "platano" es: {imp}')

print(f"\nLa cantidad de frutas que hay en la lista es de: {len(frutas) + 1}")
