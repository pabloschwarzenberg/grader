# completa el código de la función
def suma_divisores(a):
  suma=0
  i=1
  if a==1 or a==0:
       return suma, False
  while i<a:
       if a%i==0:
            suma+=i
       i+=1
       
       
  if suma==1:
       return suma, True
  else:
       return suma, False
           