# Reto en clase n°8
# Realizar un algoritmo que permita insertar elementos en un diccionario (Información de 3 estudiantes).
# El docente debe ser capaz de ingresar la siguiente información por teclado:
# ● Nombres de los estudiantes
# ● Nombre de la asignatura
# ● Nota del Laboratorio N°1
# ● Nota del Laboratorio N°2
# La ponderación del Laboratorio N°1 es de un 30% del promedio final y el Laboratorio N°2
# pondera 70% de la nota final.
# El algoritmo debe arrojar toda la información ingresada más el promedio final ponderado.
# Este promedio debe estar en un formato de punto flotante de máximo 1 decimal. Guardar

count = 0
def diccionario():
    global count
    count += 1
    Es1 = dict(
        Estudiante = input(f"\nIngrese el nombre del estudiante {count}: "),
        Asignatura = input("Ingrese la asignatura: "),
        Lab1 = float(input("Ingrese la nota del Laboratorio N°1: ")),
        Lab2 = float(input("Ingrese la nota del Laboratorio N°2: ")),
    )
    if not 1 <= Es1["Lab1"] <= 7:
        print("La nota del Laboratorio N°1 debe ser un número entre 1 y 7")
    elif not 1 <= Es1["Lab2"] <= 7:
        print("La nota del Laboratorio N°2 debe ser un número entre 1 y 7")
    else:
        P1 = round(Es1["Lab1"] * 0.3 + Es1["Lab2"] * 0.7, 1)
        Es1["Promedio Final"] = P1
        return Es1

EST = dict()
e1 = diccionario()
EST[f"Estudiante {count}"] = e1
e2 = diccionario()
EST[f"Estudiante {count}"] = e2
e3 = diccionario()
EST[f"Estudiante {count}"] = e3
print()
for clave, valor in EST.items():
    print(f"{clave}:")
    for subclave, subvalor in valor.items():
        print(f"    {subclave}: {subvalor}")