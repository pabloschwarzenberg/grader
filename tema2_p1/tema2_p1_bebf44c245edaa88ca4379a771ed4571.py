# por favor escribe aquí tu función
def es_primo(numero):
  divisor=2
  if numero==1:
    return False
  else:
    while divisor<numero:
      if numero%divisor==0:
        return False
        divisor=divisor+1
      else:
        return True
           