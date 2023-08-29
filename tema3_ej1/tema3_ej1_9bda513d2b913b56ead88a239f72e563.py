# completa el código de la función
def suma_divisores(a):
  sum = 0
  divisor = a
  while divisor > 1:
    divisor = divisor - 1
    if (a % divisor) == 0:
        sum += divisor
  # Devuelve la suma de todos los divisores de n, sin incluir n
  return sum



           