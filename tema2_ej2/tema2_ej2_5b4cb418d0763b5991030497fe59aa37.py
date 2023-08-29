# completa el código de la función

def sumDivisores(numero):
  contador = 0
  for divisor in range(1,numero-1):
    if (numero % divisor) == 0 :
      contador += divisor
 
  return contador


def amigos(a,b):
  sumaA = sumDivisores(a)
  sumaB = sumDivisores(b)
  
  return sumaA == b and a == sumaB and sumaB == a and b == sumaA
           