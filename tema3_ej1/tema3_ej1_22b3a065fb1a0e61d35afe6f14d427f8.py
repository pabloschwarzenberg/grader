def suma_divisores(a):
  resultado = 0
  divisor = a
  while divisor > 1:
    divisor = divisor - 1
    if (a % divisor) == 0:
        resultado += divisor
  if a <= 1:
        return resultado, False
  elif a==2:
        return resultado, True
  else:
        for i in range(2, a):
            if a % i == 0:
                return resultado, False
            else:
                return resultado, True
           

