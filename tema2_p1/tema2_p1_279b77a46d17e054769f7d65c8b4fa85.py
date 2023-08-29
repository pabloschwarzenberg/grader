# por favor escribe aquí tu función
def es_primo(numero):
  contador = 0
  for divisores in range(1,int(numero)+1):
    if int(numero) % divisores == 0:
      contador += 1
    else:
      contador += 0
  if contador == 2:
    return True
  if contador != 2:
    return False