# Escribir un programa que pida al usuario una palabra
# y muestre por consola el n° de veces que contiene c/ vocal

x = input("Ingrese una palabra: "); y = x.lower()

cantA = y.count("a"); cantE = y.count("e"); cantI = y.count("i"); cantO = y.count("o"); cantU = y.count("u")

print(f'La palabra "{x}" tiene en cantidad, las siguientes vocales:\n'
      f'A: {cantA}\nE: {cantE}\nI: {cantI}\nO: {cantO}\nU: {cantU}')