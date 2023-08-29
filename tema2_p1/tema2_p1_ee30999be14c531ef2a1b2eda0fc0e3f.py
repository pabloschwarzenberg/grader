# por favor escribe aquí tu función
def es_primo(numero):
  if numero==1:
    return False
  raizTruncada=int(numero**0.5)
  for divisor in range(2,raizTruncada+1):
    if numero%divisor==0:
      return False
  return True
           