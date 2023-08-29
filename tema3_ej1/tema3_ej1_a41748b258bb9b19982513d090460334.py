def suma_divisores(n):
  divisor = n
  suma = 0
  resultado=True
  while divisor > 1:
    divisor = divisor - 1
    if (n % divisor) == 0:
        suma += divisor
  if (n%2==0) or (n==1):
      resultado=False
  else:
      resultado=True
  return suma,resultado
 