# por favor escribe aquí tu función
def es_primo(numero):
  if numero==1 or numero==0:
    return False 
  elif numero==2:
   return True
  elif numero>2:
    for divisor in range(2,numero):
      if numero%divisor == 0:
        return False
      elif(numero%divisor !=0 and divisor==numero-1):
        return True
           