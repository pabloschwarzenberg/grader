# completa el código de la función
def amigos(a,b):
  divisor1=a-1
  suma1=0
  while divisor1>0:
    if a%divisor1==0:
      suma1+=divisor1
    divisor1-=1
  if b==suma1:
    suma2 = 0
    divisor2=b-1
    while divisor2>0:
      if b%divisor2==0:
        suma2+=divisor2
      divisor2-=1
    if a== suma2:
      return True
  return False