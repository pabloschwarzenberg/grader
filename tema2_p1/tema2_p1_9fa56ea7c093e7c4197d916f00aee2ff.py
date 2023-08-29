# por favor escribe aquí tu función
def es_primo(numero):
  divisor= 2
  while True:
    if numero == 1:
      return False
    if numero == divisor:
      return True
    if numero%divisor==0:
      return False

    divisor=divisor + 1       
  return