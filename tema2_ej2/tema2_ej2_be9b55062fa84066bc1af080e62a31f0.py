# completa el código de la función
def amigos(a,b):
#un numero n es divisor de a si al hacer a%n==0  // b%m==0
#son amigos si al hacer la suma de la lista n arroja b, y al hacer la suma de la lista m arroja a
  n=int(1)
  m=int(1)
  suma1=int(0)
  suma2=int(0)
  while (a>n):
    if (a%n==0):
      suma1=suma1+n 
    else:
      suma1=suma1
    n=n+1
    
  while (b>m):
    if(b%m==0):
      suma2=suma2+m
    else:
      suma2=suma2
    m=m+1  

  if(suma2==a) and (suma1==b):
    return True
  else:
    return False

           