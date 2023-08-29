def rot13(palabra):
  final= ""
  abecedario="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxhz"
  for rot in range(len(palabra)):
    variable= abecedario.find(palabra[rot])
    final += abecedario[variable+13]
  palabra= final
  return palabra