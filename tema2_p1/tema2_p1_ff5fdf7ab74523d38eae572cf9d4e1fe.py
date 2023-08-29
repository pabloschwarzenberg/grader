# por favor escribe aquí tu función
def es_primo(numero):
  if numero>=2:
    for b in range(2,numero):
      if not (numero%b):
        return False
      else:
        return True
  return False
           