# completa el código de la función
def amigos(a,b):
  i=1
  j=1
  a1=0
  b1=0
  if a==b:
    return False
  while i<=a:
    if a%i==0:
      a1=a1+i
    i=i+1
  while j<=b:
    if b%j==0:
      b1=b1+j
    j=j+1
  if a1==b1:
    return True
  else:
    return False