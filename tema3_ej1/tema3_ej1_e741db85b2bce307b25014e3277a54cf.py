# completa el código
def suma_divisores(a):
    divisor=1
    t=0
    while divisor<a:
      if a%divisor==0:
         t=t+divisor
      divisor=divisor+1
    return(t,es_primo(t))
 
def es_primo(a):
  if a==1:
     return True
  else:
     return False
  
         
    
           