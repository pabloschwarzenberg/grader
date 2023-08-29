# completa el código de la función
def amigos(a,b):
  amigoss = False
  sumaA = 0
  sumaB = 0
  divisorA = a
  divisorB = b

  while divisorA > 1:
    divisorA = divisorA - 1
    if (a % divisorA) == 0:
        sumaA += divisorA
    
  while divisorB > 1:
    divisorB = divisorB - 1   
    if (b % divisorB) == 0:
        sumaB += divisorB 
  
  if sumaB == a  and sumaA == b:
    amigoss = True
  
  return amigoss