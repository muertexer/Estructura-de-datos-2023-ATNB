// Crear una lista de números enteros
// en el cual se debe ingresar el tamaño y sus elementos por teclado.
// Se solicita ordenar ascendetente y descendentemente.
// Además solo se deben ingresar números enteros positivos
// Se solicita obtener el valor máximo y minimo de la lista

import 'dart:io';

void main() {
  List<int> num = [];
  stdout.write("Ingrese el tamaño de la lista: ");
  int size = int.parse(stdin.readLineSync()!);
  if (size > 0) {
    for (int i = 0; i < size; i++)  {
      stdout.write("Ingrese el elemento ${i+1}: ");
      int elemento = int.parse(stdin.readLineSync()!);
      if (elemento > 0) {
        num.add(elemento);
      }
      else  {
        print("El número ingresado debe ser mayor a cero");
      }
    }
    num.sort();
    print("La lista en orden ascendente es: $num");
    num = num.reversed.toList();
    print("La lista en orden descendente es: $num");
    num.sort();
    int menor = num.first;
    int mayor = num.last;
    print("El valor mayor de la lista es: $mayor");
    print("El valor menor de la lista es: $menor");
  }
  else {
    print("El número ingresado debe ser mayor a cero");
  }
}
