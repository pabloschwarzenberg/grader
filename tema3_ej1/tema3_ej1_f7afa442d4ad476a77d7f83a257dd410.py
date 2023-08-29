def suma_divisores(a):
  sum = 0
  divisor = a
  while divisor > 1:
    divisor -= 1
    if (a % divisor) == 0:
        sum += divisor

  if sum == 1:
    return (sum, True)
  else:
    return (sum, False)




