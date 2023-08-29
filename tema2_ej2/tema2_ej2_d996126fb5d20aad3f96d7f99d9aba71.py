# completa el código de la función
def amigos(a,b):
  if a==1 or b== 1 or a==b==1:
    return False
  suma1=0
  suma2=0
  divisor=1
  while divisor<a:
    if a%divisor==0:
      suma1=suma1+divisor
    divisor=divisor+1
    
   
  divisor=1
  while divisor<b:
    if b%divisor==0:
      suma2=suma2+divisor 
    divisor=divisor+1
   
  if suma1==b or suma2==a:
   return True

  else:
      return False