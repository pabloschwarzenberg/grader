# completa el código de la función
def amigos(a,b):
  divisor=a-1
  divisor2=b-1
  suma=0
  suma2=0
  while divisor>0:
    if a%divisor==0:
      suma+=divisor
    divisor-=1
  if b == suma:
    while divisor2>0:
      if b%divisor2==0:
        suma2+=divisor2
      divisor2-=1
  if a==suma2:
    return True
  else:
    return False           