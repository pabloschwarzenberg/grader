# completa el código de la función
def suma_divisores(a):
  x=0
  divisor=a-1
  if a==1:
    return 0,False
  while divisor>=1:
    if a%divisor==0:
      x+=divisor
    divisor-=1
  if x>1:
    return x,False
  if x==1:
    return 1,True
     
    
  
  
    
  
  
  
           