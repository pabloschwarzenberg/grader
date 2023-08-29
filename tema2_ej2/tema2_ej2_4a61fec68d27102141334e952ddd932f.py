# completa el código de la función
def amigos(a,b):
  amigoss = False
  suma1 = 0
  suma2 = 0
  divisor1 = a
  divisor2 = b

  while divisor1 > 1:
    divisor1 = divisor1 - 1
    if (a % divisor1) == 0:
        suma1 += divisor1
    
  while divisor2 > 1:
    divisor2 = divisor2 - 1   
    if (b % divisor2) == 0:
        suma2 += divisor2 
  
  if suma2 == a  and suma1 == b:
    amigoss = True
  
  return amigoss   