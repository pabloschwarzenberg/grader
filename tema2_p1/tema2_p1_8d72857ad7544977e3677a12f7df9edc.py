# por favor escribe aquí tu función
def es_primo(n):
  if n == 1 or n == 0:
    return False
  elif n == 2:
    return True
  elif n>2:
    for divisor in range(2,n):
      if n % divisor == 0:
        return False
      elif n % divisor != 0 and divisor == n - 1:
        return True

print(es_primo(211))
           