# Calcular la circunferencia y superficie de un circulo
# 1. Pseudocodigo
# 2. Diagrama flujo o N-S
# 3. Algoritmo en python

# A = pi * r²
# P = 2 * pi * r

pi = 3.14
r = float(input("Ingrese el radio de la circunferencia: "))

A = pi * r ** 2
P = 2 * pi * r

print("\nLa superficie es:\t", round(A, 3), "\nLa circunferencia es:\t",round(P, 3))


