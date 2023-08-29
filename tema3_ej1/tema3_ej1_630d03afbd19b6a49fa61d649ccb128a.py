# completa el código de la función
def suma_divisores(a):
  divisor = a
  suma = 0
  resultado=True
  while divisor > 1:
    divisor = divisor - 1
    if (a % divisor) == 0:
        suma += divisor
  if (a%2==0) or (a==1):
       resultado=False
  else:
      resultado=True
  return suma,resultado