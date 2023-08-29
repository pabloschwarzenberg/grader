# completa el código de la función
def suma_divisores(a):
  divisor=1
  z=[]
  while divisor<a:
    if a%divisor==0:
        z.append(divisor)
    divisor=divisor+1
  j=sum(z)
  if j==1:
    return (j,True)
  else:
    return (j,False)