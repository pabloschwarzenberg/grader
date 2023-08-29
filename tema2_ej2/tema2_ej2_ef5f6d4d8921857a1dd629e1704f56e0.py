# completa el código de la función
def amigos(a,b):
  if a == b:
    return False
  else:
    highest = max(a, b)
    i = 1
    sum_a = 0
    sum_b = 0
    while i <= highest:
      if a % i == 0:
        sum_a += i
      if b % i == 0:
        sum_b += i
        
      i += 1

    if sum_a == sum_b:
        return True
    return False
