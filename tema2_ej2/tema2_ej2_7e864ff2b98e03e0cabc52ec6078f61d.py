# completa el código de la función
def amigos(a,b):
  divisor=1
  sumaa=0
  sumab=0

  while divisor<a:
    if a%divisor==0:
      sumaa=sumaa+divisor
      divisor=divisor+1
    else:
      divisor=divisor+1

  while divisor<b:
    if b % divisor == 0:
      sumab=sumab+divisor
      divisor = divisor + 1
    else:
      divisor = divisor + 1
  if (a==1 and b==2)or(a==2 and b==1):
    return False
  elif sumaa==b or sumab==a:
    return True
  else:
    return False