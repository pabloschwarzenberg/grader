def numero_perfecto(a,num_per=False):
  suma = 0
  divisor = a
  while divisor > 1:
    divisor = divisor -1
    if (a % divisor) == 0:
      suma += divisor
  if suma == a:
    num_per = True
  return num_per
  



           