# completa el código de la función
def suma_divisores(a, n=2):
  sum = 0
  divisor = a     
  while divisor > 1:
    divisor = divisor - 1
    if (a % divisor) == 0:
        sum += divisor
  if a==1:
    return sum,False
  elif a % n !=0:
    return sum,True
  else:
    return sum,False
           