# completa el código de la función
def amigos(a,b):
  n=1
  m=1
  sumaa=0
  sumab=0
  while(n<a)and(m<b):
    if(a%n==0):
      sumaa=n+sumaa
    n=n+1
    if(b%m==0):
      sumab=n+sumab
    m=m+1
    
  if(sumaa==b)or(a==sumab): 
    return True
  else: 
    return False
       

           