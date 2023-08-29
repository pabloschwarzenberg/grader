# completa el código de la función
def suma_divisores(n):
  suma=0
  for i in range(1,n):
    if n%i==0:
      suma+=i
      
      
  primo=suma==1
  
  return suma,primo
           