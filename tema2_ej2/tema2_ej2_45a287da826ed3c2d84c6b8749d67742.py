# completa el código de la función
def amigos(a,b):
  sumaA = 0

  sumaB = 0

  for n in range(1,a):

    if a % n == 0:

      sumaA += n

  for x in range(1,b):

      if b % x == 0:

        sumaB += x

        

  if sumaA == b and sumaB == a:

    return True

  

  else:

    return False
           