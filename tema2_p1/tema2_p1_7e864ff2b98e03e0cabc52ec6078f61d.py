# por favor escribe aquí tu función
def es_primo(numero):
  divisor=1
  contadordivisores=0
  while divisor<=numero:
    if numero%divisor==0:
      contadordivisores=contadordivisores+1
      divisor=divisor+1
    else:
      divisor=divisor+1
  if contadordivisores==2:
    return True
  else:
    return False