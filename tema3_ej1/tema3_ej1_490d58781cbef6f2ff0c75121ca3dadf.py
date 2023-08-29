# completa el código de la función
def suma_divisores(a):
  suma=0
  i=1
  while i<a:
    if a%i==0:
      suma=suma+i
    i=i+1
  if suma==1:
      return suma, True
  else:
      return suma, False
  if a ==0 or a==1:
      return 0, False
  
   
  
           