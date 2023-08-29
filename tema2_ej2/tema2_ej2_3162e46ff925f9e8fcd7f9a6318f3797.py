import random
import math
a= random.random()
b= random.random()
a= math.trunc(a)
b= math.trunc(b)
def amigos(a,b):
  divisores_a= int(0)
  divisores_b= int(0)
  for n in range(1, a):
    if(a % n == 0):
      divisores_a+= n
  for f in range(1, b):
    if(b % f == 0):
      divisores_b+= f
  if (divisores_a == b and divisores_b == a):
    return True
  else:
    return False
    
amigos(a,b)