def suma_divisores(a):
  suma = 0
  divisor = a
  while divisor > 1:
      divisor = divisor -1
      if a % divisor == 0:
          suma += divisor
          
  if suma == 1:
      suma_divisores = (suma,True)
  else:
      suma_divisores = (suma,False)
        
  return suma_divisores         