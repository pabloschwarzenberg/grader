# por favor escribe aquí tu función

def es_primo(numero):
  divisor=1
  divisores=0
  while divisor<=numero:
    if numero%divisor==0:
      divisores=divisores+1
    divisor=divisor+1
  if divisores==2:
    return True
  else: 
    return False
 
