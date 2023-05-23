// Crear dos listas:
// a. La primera lista debe ser generada de forma aleatoria y tener 5
// elementos
// b. La segunda se debe ingresar por teclado (Debe tener 5 elementos
// enteros)
// c. Concatenar las dos listas anteriores
// d. Insertar en la 7°,8° y 9° posición los elementos 14,20,7 (agregando todos
// los elementos de una sola vez, utilizando un método en específico)
// e. Obtener el promedio de la lista obtenida anteriormente.
// f. Por último ordenar de forma descendente la lista.

import 'dart:math';
import 'dart:io';

void main(){
Random random = Random();
List l1 = List.generate(5, (index) => random.nextInt(20));
print("Lista 1: $l1");
print("Ingrese 5 números:");
List l2 = List.generate(5, (index) => stdin.readLineSync());
print("Lista 2: $l2");

// Intento de cambio de lista con string a lista con int
// List<int> l4 = List<int>.from(l2);

// for(int i = 0;i > l2.length; i++){
//   l2.();
// }

List l3 = l1 + l2;
print("La lista concatenada es: $l3");
List<int> val = [14,20,7];
l3.replaceRange(6,9,val);
print("La lista con valores insertados es: $l3");

// No se puede ordenar de manera descendente hasta que todos los valores de la lista sean enteros
print("La lista de forma descendente: $l3");



}

