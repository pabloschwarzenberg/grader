# completa el código de la función
def suma_divisores(a):
  i=1
  suma=0
  if a==1 or a==0:
    return suma,False
  while i<a:
    if a%i==0:
        suma+=i
    i+=1
  
  if suma==1:
    return suma,True
  else:
   return suma,False