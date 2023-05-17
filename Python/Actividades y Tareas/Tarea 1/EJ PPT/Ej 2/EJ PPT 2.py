# Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario
# 1. Pseudocódigo
# 2. Diagrama flujo o N-S
# 3. Algoritmo en python

# Ej: 28 = 11100 & 95 = 1011111

def DecToBin(dec):
    bin = ""
    while dec > 0:
        resto = int(dec % 2)
        dec = dec // 2
        bin = str(resto) + bin
    return bin

dec = int(input("Ingrese el número entero decimal para convertir en binario: "))
bin = DecToBin(dec)
print(f"\nEl número {dec} es {bin} en binario")