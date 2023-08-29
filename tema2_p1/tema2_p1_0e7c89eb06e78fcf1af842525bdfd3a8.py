# por favor escribe aquí tu función
def es_primo(numero):
  if numero == 1:
    return False
    
  for x in range(2, numero):
    if numero % x == 0:
      return False
  return True    

           