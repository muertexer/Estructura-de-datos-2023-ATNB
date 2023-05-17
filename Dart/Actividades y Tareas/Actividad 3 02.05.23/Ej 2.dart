// Crear un arreglo de tamaño aleatorio (entre 10 a 30 elementos).
// Los elementos también deben ser aleatorios (de 0 a 10).
// Además se solicita ordenarlo de forma ascendente
// Luego ordenar ese mismo arreglo de forma aleatoria

import 'dart:math';

void main() {
  Random azar = Random();
  int size = azar.nextInt(21) + 10;
  List<int> arr = List.generate(size, (index) => azar.nextInt(11));

  arr.sort();
  print("El arreglo de forma ascendente: \n$arr");
  arr.shuffle();
  print("\nEl arreglo de forma aleatoria: \n$arr");
}