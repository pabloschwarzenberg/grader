# completa el código de la función
def amigos(a,b):
  if a == b:
    return False
  sum = 0
  divisor = b
  while divisor > 1:
      divisor = divisor - 1
      if (b % divisor) == 0:
          sum += divisor
  if divisor == a:
      return False
  elif divisor != a:
      return True


           