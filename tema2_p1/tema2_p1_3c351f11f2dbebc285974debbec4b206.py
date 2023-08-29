# por favor escribe aquí tu función
def es_primo(numero):
  if 1==numero:
    return False
  for n in range(2, numero):
    if numero % n == 0:
      return False
  return True 

           