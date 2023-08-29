# por favor escribe aquí tu función
def es_primo(numero):
  divisor = 2
  c = 0
  if numero == 1:
    return False
  while divisor < numero:
    if numero % divisor == 0 and c == 0:
      c += 1
      return False
      break
    if numero % divisor != 0 and c == 0:
      divisor += 1
  else:
    return True
    
  