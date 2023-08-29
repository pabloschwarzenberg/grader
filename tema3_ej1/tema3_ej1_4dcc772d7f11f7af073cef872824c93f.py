# completa el código de la función
def suma_divisores(a):
  sum = 0
  divisor = a
  while divisor > 1:
      divisor = divisor - 1
      if a % divisor == 0:
          sum += divisor

  if sum == 1:
     suma_divisores = (sum,True)
  else:
     suma_divisores = (sum,False)

  return suma_divisores
  
           