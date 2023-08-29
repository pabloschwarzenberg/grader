# completa el código de la función
def amigos(a,b):
  A=0
  B=0
  n=1
  while True:
    if(n<a and a/n==a//n):
      A=A+n
    if(n<b and b/n==b//n):
      B=B+n
    if(n>a and n>b):
      break
    n=n+1
  if(A==b and B==a):
    return True
  else:
    return False
    