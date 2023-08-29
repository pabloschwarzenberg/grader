# por favor escribe aquí tu función
def es_primo(numero):
  divisor= 2
  while True:
    if numero == 1:
      return False
      break
    if numero == divisor:
      return True
      break
      
    if numero%divisor==0:
      return False
      break

    divisor=divisor + 1       
  return
           