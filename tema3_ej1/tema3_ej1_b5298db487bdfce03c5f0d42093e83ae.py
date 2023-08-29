import math
def suma_divisores(a):
    divisores = [1]


    if a==1:
      return 0, False
    for i in range(2,a-1):
      if a%i == 0:
          divisores.append(i)
    if a <=1:
        return False
    for i in range (2,math.ceil(math.sqrt(a))+1):
        if a % i == 0 and i != a:
            return sum(divisores), False
    return sum(divisores), True
