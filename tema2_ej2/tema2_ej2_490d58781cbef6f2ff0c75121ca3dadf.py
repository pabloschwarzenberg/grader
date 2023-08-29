def amigos(a,b):
  if a==b:
    return False
  if a==0 or a==1 or b==0 or b==1:
    return False
  x=a+1
  y=b+1
  divisor=2
  while divisor<a:
    if a%divisor==0:
      x=x+divisor
    divisor=divisor+1
  divisor=2
  while divisor<b:
    if b%divisor==0:
      y=y+divisor
    divisor=divisor+1
  if x==y:
    return True
  else:
    return False
amigos(6,8)
           