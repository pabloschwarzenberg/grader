def amigos(a,b):
  divisor=2
  if a==1 and b==2:
    return False
  while divisor<a and divisor<b:
    if a%divisor==0:
        if divisor==b:
          return True
        else:
          return False
    if b%divisor==0:
      if divisor==a:
        return True
      else:
        return False
    divisor+=1

           