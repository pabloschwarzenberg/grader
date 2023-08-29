# por favor escribe aquí tu función
def es_primo(numero):
  if numero ==2:
      return True
  else:
    for i in range(2,numero):
        if not (numero %i == 0):
            return True
        else:
            return False
    return False    