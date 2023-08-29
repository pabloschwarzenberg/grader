# por favor escribe aquí tu función
def es_primo(numero):
  if numero==1:
    return False
  divisor=2
  while divisor<numero:
    if numero%divisor==0:
      return False
    divisor=divisor+1
  return True
    
  
