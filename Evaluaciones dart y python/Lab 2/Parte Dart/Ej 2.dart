// Crear dos listas en Dart:
// a. La primera lista debe tener los siguientes 10 elementos:
// [3,4,7,9,8,5,1,2,5,7]
// b. La segunda lista igual debe contener 10 elementos, pero deben ser
// generados de forma aleatoria. (Solo números aleatorios negativos
// del -1 al -5)
// c. Luego sumar ambas listas e imprimir la lista resultante
// d. Por último, se necesita remover el séptimo y octavo elemento de la
// lista anterior e imprimir la nueva lista obtenida.
import 'dart:math';

void main() {
  List<int> lista1 = [3,4,7,9,8,5,1,2,5,7];
  List<int> lista2 = [];
  int valNeg = (Random().nextInt(5)+1)*-1;
  for (int i = 0 ; i < 10 ; i++) {
    lista2.add(valNeg);
  }

  print("Lista 1: $lista1");
  print("Lista 2: $lista2");

  List<int> lista3 = [];

  for (int i = 0; i < 10; i++) {
    int sum = lista1.elementAt(i) + lista2.elementAt(i);
    lista3.add(sum);
  }
  print("Suma listas: $lista3");

  lista3.removeRange(6, 8);
  print("Lista resultante con el séptimo y octavo elemento eliminado: $lista3");
}



