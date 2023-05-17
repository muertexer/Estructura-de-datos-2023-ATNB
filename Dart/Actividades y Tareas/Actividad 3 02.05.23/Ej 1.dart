// Solicitar una lista de números enteros al usuario por teclado, y luego
// sumar cada elemento de la lista obtenida.
import 'dart:io';


void main() {
  print('Ingrese la lista de números enteros, separados por un espacio:');
  String entrada = stdin.readLineSync()!;
  List<int> numeros = entrada.split(' ').map((e) => int.parse(e)).toList();
  print('\nLa lista de números ingresada es: $numeros');

  int  sum  = 0;
  for (int numb in numeros) {
    sum += numb;
  }
  print("\nLa suma de c/ elemento en la lista es: $sum");
}