# Diseña un programa que solicite el valor de los tres lados de un triángulo y calcule el valor de su área y perímetro
# Recuerda que el área A de un triángulo puede calcularse a partir de sus tres lados, a,b, y c, así:
# A = ( s*(s-a)*(s-b)*(s-c) )**(1/2) , donde s = (a+b+c)/2
# 1. Pseudocodigo
# 2. Diagrama flujo o N-S
# 3. Algoritmo en python

a, b, c = input('Ingrese los 3 lados del triángulo, separadas por comas : ').split(",")
a, b, c = float(a), float(b), float(c)

s = (a+b+c)/2
area = ( s*(s-a)*(s-b)*(s-c) )**(1/2)
perimetro = a + b + c

print(f"El área del triángulo es: {round(area, 3)} y el perimetro es: {perimetro}")