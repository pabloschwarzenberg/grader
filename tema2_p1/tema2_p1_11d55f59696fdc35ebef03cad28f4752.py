# por favor escribe aquí tu función
def es_primo(numero):
  x = numero
  z = 0
  for y in range(x):
    c = x % (y+1)
    if c == 0:
      z += 1
  if z == 2:
    return True
  else:
    return False
           