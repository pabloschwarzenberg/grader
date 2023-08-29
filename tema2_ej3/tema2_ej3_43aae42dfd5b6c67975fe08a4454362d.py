def numero_perfecto(a):
  divisor=1
  z=[]
  while divisor<a:
    if a%divisor==0:
        z.append(divisor)
    divisor=divisor+1
  j=sum(z)
  if j==a:
    return True
  else:
    return False