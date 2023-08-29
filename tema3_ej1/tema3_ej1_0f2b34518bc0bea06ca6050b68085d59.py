# completa el código de la función
def suma_divisores(a,primos=False):
  suma=0
  divisor = a
  while divisor >1:
    divisor = divisor -1
    if (a % divisor) == 0:
      suma += divisor
  if suma == 1:
    primos = True
  return (suma,primos)
print(suma_divisores(13))