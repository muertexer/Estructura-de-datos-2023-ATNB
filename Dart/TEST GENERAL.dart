void main() {
  List<int> lista = [5, 2, 8, 1, 9, 20, 15];
  lista.sort();
  int menor = lista.first;
  int mayor = lista.last;
  print("El elemento mayor de la lista es: $mayor");
  print("El elemento menor de la lista es: $menor");
}