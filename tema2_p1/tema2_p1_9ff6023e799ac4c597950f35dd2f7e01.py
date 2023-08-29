from random import *
def es_primo(a):
  primo=True
  divisor =2
  if a==1:
    primo=False
  while divisor<a and primo:
    if a % divisor == 0:
      primo=False
    divisor += 1    
  return(primo) 
a=randint(1,999)
print(es_primo(a))

           