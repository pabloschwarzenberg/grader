def adn(string,n):
  repeticiones = {}
  secuencia = string
  Ninguno= True

  for prueba in range(len(secuencia)-(n)+1):
    if secuencia[prueba:prueba+n] not in repeticiones:
      repeticiones[secuencia[prueba:prueba+n]]= 1
    else:
      repeticiones[secuencia[prueba:prueba+n]]= 1+ repeticiones[secuencia[prueba:prueba+n]]

  for chequeo in repeticiones:
    if repeticiones[chequeo] == 1:
      print(chequeo)
      Ninguno= False

  if Ninguno:
    print("ninguna")

a=input("Ingrese la secuencia:")
b=int(input("Ingrese el largo:"))
adn(a,b)