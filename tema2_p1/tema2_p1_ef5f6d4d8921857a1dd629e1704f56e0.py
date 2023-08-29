# por favor escribe aquí tu función
def es_primo(numero):
  if numero == 0 or numero == 1:
    return False
  
  prime_factors = 0
  i = 1
  while i <= numero:
    if numero % i == 0:
      prime_factors += 1
    if prime_factors > 2:
      return False
    i += 1
  return True
           