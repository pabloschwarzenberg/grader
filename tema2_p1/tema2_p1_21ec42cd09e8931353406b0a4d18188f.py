# por favor escribe aquí tu función
def es_primo(numero):
  if numero<2:
    return False 
  elif numero==2:
    return True
  else:
    for N in range(2,numero):
      if numero%N==0:
        return False
      elif N==numero-1:
        return True
           