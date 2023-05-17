# Determine la distancia entre dos puntos en el espacio (x1,y1, z1) y (x2, y2, z2).
# 𝑑 = √( (𝑥1 − 𝑥2)^2 + (𝑦1 − 𝑦2)^2 + (𝑧1 − 𝑧2)^2 )

# 1. Pseudocodigo
# 2. Diagrama flujo o N-S
# 3. Algoritmo en python

x1, y1, z1 = input('Ingrese las coordenadas del PRIMER vector en r3, separadas por comas : ').split(",")
x1, y1, z1 = float(x1), float(y1), float(z1)

x2, y2, z2 = input('Ingrese las coordenadas del SEGUNDO vector en r3, separadas por comas : ').split(",")
x2, y2, z2 = float(x2), float(y2), float(z2)

Distancia = ( (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2 )**(1/2)

print("\nLa distancia entre los puntos es:", Distancia)



