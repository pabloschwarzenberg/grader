# completa el código de la función
from random import *
a=randint(1,999)
b=randint(1,999)
def amigos(a,b):
  numa=0
  numb=0
  divisora=2
  divisorb=2
  while divisora<a :
    if (a%divisora)==0 :
        numa+=divisora
        divisora = divisora+1
        
    else:
        divisora=divisora+1
  while divisorb<b:
    if (b%divisorb)==0:
        numb+=divisorb
        divisorb+=1
    else:
        divisorb+=1
  if numa==numb and ((numa or numb)!=1) :
    return False
  else:
    return True

amigos(a,b)
  
           