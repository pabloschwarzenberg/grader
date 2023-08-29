# completa el código de la función
def amigos(a,b):
  x=0
  y=0
  for n in range(1,a):
    if a%n==0 and n!=a:
      x=x+n
  for m in range(1,b):
    if b%m==0 and m!=b:
      y=y+m
  if x==b and y==a:
    return True
  else:
    return False
           