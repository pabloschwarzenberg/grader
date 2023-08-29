# por favor escribe aquí tu función
def es_primo(numero):
  cont = 0
  for i in range(2,numero):
    if numero%i == 0:
      cont += 1
  if cont == 0 and numero != 1:
    return True
  else:
    return False
           