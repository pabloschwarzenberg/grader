# por favor escribe aquí tu función
def es_primo(numero):
  if numero == 1:
    return False
  if numero == 2:
    return True
  for divisor in range(2,numero):
    Res = numero%divisor
    if Res == 0:
      return False
  return True