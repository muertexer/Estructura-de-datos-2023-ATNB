# Diseña un programa que, dado un número real que debe representar la calificación numérica de un examen,
# proporcione la calificación cualitativa correspondiente al número dado.
# La calificación cualitativa será una de las siguientes:
# “Reprobado” (nota menor a 4,0), “Aprobado” (nota mayor a 4,0, pero menor a 5,0),
# “Notable” (nota mayor a 5,0 pero menor a 6,0), “Sobresaliente” (nota mayor a 6,0)

# 1. Pseudocodigo
# 2. Diagrama flujo o N-S
# 3. Algoritmo en python

nota = float(input("Ingrese la nota a calificar: "))
if 1 <= nota <= 7:
    if nota < 4:
        print("Reprobado")
    elif 4 <= nota < 5:
        print("Aprobado")
    elif 5 <= nota < 6:
        print("Notable")
    elif 6 <= nota <= 7:
        print("Sobresaliente")
else: print("La nota ingresada debe ser igual o estar entre 1 y 7")