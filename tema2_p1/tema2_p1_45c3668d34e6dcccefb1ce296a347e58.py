# por favor escribe aquí tu función
def es_primo(numero):
  if numero<=1:
    return False
  for a in range(2,numero):
    if numero % a==0:
      return False
  return True
