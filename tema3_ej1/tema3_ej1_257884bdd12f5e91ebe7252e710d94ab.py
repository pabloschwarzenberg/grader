def suma_divisores(n):
  sum = 0
  divisor = n
  while divisor > 1:
    divisor = divisor - 1
    if(n % divisor) == 0:
      sum +- divisor
      return sum