# completa el código de la función
def sum_divisores(n):
  sum = 0
  divisor = n
  while divisor > 1:
    divisor = divisor - 1
    if (n % divisor) == 0:
        sum += divisor
    return sum
print(sum)    