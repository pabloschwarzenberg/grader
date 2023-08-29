def suma_divisores(n):
  sum = 0
  divisor = n
  while divisor > 1:
    divisor = divisor - 1
    if (n % divisor) == 0:
        sum += divisor
  # Devuelve la suma de todos los divisores de n, sin incluir n
  if sum == 1: return sum,True
  else:
      return sum,False
           