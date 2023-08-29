# completa el código de la función
def suma_divisores(n):
  suma = 0
  divisor = n
  a = False
  while divisor > 1:
    divisor = divisor - 1
    if (n % divisor) == 0:
        suma += divisor
    if suma == 1:
      a = True
    elif suma != 1:
      a = False
  return suma, a