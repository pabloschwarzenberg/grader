# completa el código de la función
def suma_divisores(a):
 if a==1:
  return (0,False)
 i=1
 x=1
 suma=0
 while i<a:
  if a%x==0:
   suma=suma+x
  x=x+1 
  i=i+1
 if suma==1:
  return (suma,True)
 else:
  return (suma,False)        