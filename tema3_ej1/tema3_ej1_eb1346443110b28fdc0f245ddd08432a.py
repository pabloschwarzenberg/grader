def suma_divisores(a):
  suma = 0
  divisor = a
  x = False
  while divisor > 1:
    divisor = divisor - 1
    if (a % divisor) == 0:
        suma += divisor
  if suma == 1:
    x = True
  return suma, x

print(suma_divisores(13))
  