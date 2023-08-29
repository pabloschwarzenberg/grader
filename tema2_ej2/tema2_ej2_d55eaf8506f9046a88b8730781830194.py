# completa el código de la función
def amigos(a,b):
  if a==b:
    return False
  i=1
  sum1=0
  sum2=0
  while i<=a:
    if a%i==0:
      sum1=sum1+i
    i=i+1
  i=1
  while i<=b:
    if b%i==0:
      sum2=sum2+i
    i=i+1
  if sum1==sum2:
    return True
  else:
    return False