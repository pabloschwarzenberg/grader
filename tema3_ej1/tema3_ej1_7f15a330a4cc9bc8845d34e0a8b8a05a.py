# completa el código de la función
def suma_divisores(c, n=2):
  sum = 0
  divisor = c     
  while divisor > 1:
    divisor = divisor - 1
    if (c % divisor) == 0:
        sum += divisor
  if c==1:
    return sum,False
  elif c % n !=0:
    return sum,True
  else:
    return sum,False
           