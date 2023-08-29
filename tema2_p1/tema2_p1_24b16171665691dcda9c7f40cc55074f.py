# por favor escribe aquí tu función
def es_primo(numero_primo):
  if numero_primo <=1:
    return False
  for los_valores in range(2,numero_primo):
    if numero_primo % los_valores == 0 :
      return False
  return True
