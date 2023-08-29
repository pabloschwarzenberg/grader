# por favor escribe aquí tu función
def es_primo(numero):
  if numero < 2:
    return False
  x = int(2)
  while numero != x:
    if numero % x == 0:
      return False
    else:
      x = x + 1
  if numero == x:
    return True


    
           