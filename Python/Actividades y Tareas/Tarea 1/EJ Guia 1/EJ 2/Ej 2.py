# Elaborar un algoritmo para obtener los números primos comprendidos entre 1 y 500.

# 1. Pseudocodigo
# 2. Diagrama flujo o N-S
# 3. Algoritmo en python

def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = []
for i in range(1, 500):
    if primo(i):
        primos.append(i)

print("Hay {} números primos entre 1 y 500 y estos son:".format(len(primos)))
for i in range(0, len(primos), 5):
    print("{:4d} {:4d} {:4d} {:4d} {:4d}".format(*primos[i:i+5]))