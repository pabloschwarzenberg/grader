# completa el código de la función
def sum_divisores(a):
  sum = 0
  divisor = a

  while divisor > 1:
    divisor = divisor - 1
    if (a % divisor) == 0:
        sum += divisor
  if sum <= 1:
        return False
    elif sum == 2:
        return True
    else:
        for i in range(2, sum):
            if sum % i == 0:
                return False
        return True  



  