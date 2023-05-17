Persona1, Rut1 = input("Ingrese nombre de la persona 1 y su rut, separados por una coma: ").split(",")
Persona2, Rut2 = input("Ingrese nombre de la persona 2 y su rut, separados por una coma: ").split(",")
Persona3, Rut3 = input("Ingrese nombre de la persona 3 y su rut, separados por una coma: ").split(",")
Persona4, Rut4 = input("Ingrese nombre de la persona 4 y su rut, separados por una coma: ").split(",")
Persona5, Rut5 = input("Ingrese nombre de la persona 5 y su rut, separados por una coma: ").split(",")

Nombres = [Persona1, Persona2, Persona3, Persona4, Persona5]
Ruts = [Rut1, Rut2, Rut3, Rut4, Rut5]

print("\nArrays:\n")

print(*Nombres, sep = ', ')
print(*Ruts, sep = ', ')

print("\nArrays ordenados:\n")
print(*sorted(Nombres), sep = ', ')
print(*sorted(Ruts), sep = ', ')