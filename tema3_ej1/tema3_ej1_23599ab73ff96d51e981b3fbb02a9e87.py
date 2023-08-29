def sum_divisores(n):
  sum = 0
  divisor = n

  while divisor > 1:
    divisor = divisor - 1
    if (n % divisor) == 0:
        sum += divisor

  # Devuelve la suma de todos los divisores de n, sin incluir n
  return sum
 print(sum_divisores(0))