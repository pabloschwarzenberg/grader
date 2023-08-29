# completa el código de la función
def amigos(a,b):
 sumaa=0
 sumab=0
 n=1
 r=1
 while(n<=(a-1)): 
  if(a%n==0):
   sumaa=sumaa+n
  n=n+1
 while(r<=(b-1)):
  if(b%r==0):
   sumab=sumab+r
  r=r+1
 if(sumaa==b and sumab==a):
  return True
 else:
  return False
           