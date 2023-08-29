def suma_divisores(n):
  divisor = n
  sum = 0
  while divisor > 1:
    divisor -= 1
    if (n % divisor) == 0:
        sum += divisor

  if sum == 1:
    return (sum, True)
  else:
    return (sum, False)

