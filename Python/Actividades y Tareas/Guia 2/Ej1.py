# 1. Crear una lista de diccionarios llamada pacientes donde cada diccionario representa a
# un paciente con su informacion personal. Se solicita crear una lista de 4 diccionarios. ´
# Agregar la informacion mediante teclado. La informaci ´ on personal de cada paciente es: ´
# a) Nombre (tipo String)
# b) Edad (tipo Int)
# c) Peso (tipo Float)
# d) Sintomas (Lista de String)
# Ademas realizar una b ´ usqueda en la lista de pacientes para encontrar un paciente en ´
# espec´ıfico por nombre y mostrar su ficha personal correspondiente.


count = 0
def patient():
    global count
    count += 1
    Pas = dict(
        Nombre = input(f"\nIngrese el nombre del paciente {count}: "),
        Edad = int(input("Ingrese su edad: ")),
        Peso = float(input("Ingrese su peso (Kg): ")),
        Sintomas = list(input("Ingrese los sintomas, separados por un guión: ").split("-")),
    )
    return Pas

ListPatient = list()
e1 = patient()
ListPatient.append(e1)
e2 = patient()
ListPatient.append(e2)
# e3 = patient()
# ListPatient.append(e3)
# e4 = patient()
# ListPatient.append(e4)

print("\nPacientes:\n")
for dicc in ListPatient:
    print(dicc["Nombre"])

key = "Nombre"
while True:
    value = input("\nIngrese un nombre de un paciente ingresado, para mostrar su ficha personal correspondiente: ")
    found = False
    print("\nBusqueda:\n")
    for dicc in ListPatient:
        if dicc.get(key) == value:
            for clave, valor in dicc.items():
                if clave == "Sintomas":
                    print(f"{clave}:")
                    for i, sintoma in enumerate(valor):
                        print(f"{i + 1}. {sintoma}")
                else: print(f"{clave}: {valor}")
                found = True
    if not found:
        print(f'\nNo se encontró ningún paciente ingresado como "{value}", intente nuevamente\n')
    else: break

