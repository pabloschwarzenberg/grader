# por favor escribe aquí tu función
def es_primo(numero):
  if numero == 1:
    return False
  x = 2
  TempA = 0
  while x < numero:
    if numero % x == 0:
      TempA = 1
      break
    x += 1
  if TempA == 0:
    return True
  else:
    return False
