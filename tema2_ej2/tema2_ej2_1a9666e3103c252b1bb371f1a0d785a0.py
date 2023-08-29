# completa el código de la función
def amigos(a,b):

    A=[]

    B=[]

    for i in range(1,a):

      if a%i==0:

        A.append(i)

    for i in range(1,b):

      if b%i==0:

        B.append(i)

    sumaA=0

    sumaB=0

    for x in A:

        sumaA+=x

    for x in  B:
  
      sumaB+=x

    if sumaA == b and sumaB == a:

       return True

    else:

        return False
           