# completa el código de la función
def suma_divisores(a):
  suma=0
  x=""
  if a!=1:
    for i in range(1,(a-1)):
      if a%i==0:
        suma+=i
        
  if suma==1:
    x=True
  else:
    x=False
  
    
  return suma,x
           