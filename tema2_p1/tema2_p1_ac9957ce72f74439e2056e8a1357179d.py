# por favor escribe aquí tu función
def es_primo(numero):
  primacidad = False
  contador = 0
  for i in range(numero):
    division = numero%(i+1)
    if division == 0:
      contador += 1
    if contador == 2:
      primacidad = True
    elif contador != 2:
      primacidad = False
  #Oops, creí que era primo xD
  #if numero == 1:
  #  primacidad = True
  return primacidad

#es_primo(int(input("Ingrese numero a comprobar: ")))