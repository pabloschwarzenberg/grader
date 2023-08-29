def adn(string):
  secuencia = string.lower()
  chequeo= True
  for prueba in range(len(secuencia)):
    if secuencia[prueba] != "a" and secuencia[prueba] !=  "c" and secuencia[prueba] != "t" and secuencia[prueba] != "g":
      chequeo= False
  if chequeo:
    print("La secuencia", string, "es correcta")
  else:
    print("La secuencia", string, "es incorrecta")

variable=input("Ingrese su secuencia:")
adn(variable)