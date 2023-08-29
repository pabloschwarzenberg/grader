def adn(string1,string2):
  secuencia = string1
  final=""
  Ninguno= True
  recorrido=0

  while len(final)<len(secuencia):
    for ciclos in range(len(string2)):
      conteo= secuencia[recorrido:].find(string2[ciclos])
      recorrido +=conteo+1
      final += "_"*conteo + string2[ciclos]
  print(final)




a=input("Ingrese la secuencia 1:")
b=input("Ingrese la secuencia 2:")
adn(a,b)