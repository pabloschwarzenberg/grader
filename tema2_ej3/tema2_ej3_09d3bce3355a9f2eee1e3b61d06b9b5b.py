def numero_perfecto(a):
  divisor = a
  suma = 0
  resultado=True
  while divisor > 1:
    divisor = divisor - 1
    if (a % divisor) == 0:
        suma += divisor
  if suma==a:
      resultado=True
  else:
      resultado=False
  return resultado
