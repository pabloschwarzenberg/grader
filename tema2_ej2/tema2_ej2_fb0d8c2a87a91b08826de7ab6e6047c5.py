# completa el código de la función
def amigos(a,b):
  divisor=1
  suma=0
  while(divisor<a):
    if(a%divisor==0):
      suma+=divisor
    divisor=divisor+1   
  if(suma==b):
    return True
  else:
    return False
  divi=1
  sumas=0
  while(divi<b):
    if(b%divi==0):
      sumas+=divi
    divi=divi+1   
  if(sumas==a):
    return True
  else:
    return False
      
           