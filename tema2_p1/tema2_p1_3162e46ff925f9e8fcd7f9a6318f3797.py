import random
import math
n= random.random()
n= math.trunc(n)
def es_primo(n):
  divisores= []
  for j in range(1, n+1):
    if(n % j == 0):
      divisores.append(j)
    else:
      continue
  if(len(divisores) == 2):
    return True
  else:
    return False
    
es_primo(n)