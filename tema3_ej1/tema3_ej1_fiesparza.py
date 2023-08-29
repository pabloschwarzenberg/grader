# completa el código de la función
def suma_divisores(a):
  suma=0
  i=1
  while i <a:
      
       if a%i!=0:
           suma=suma
           i=i+1
       else:
            suma=suma+i
            i=i+1
  
  if a==1:
     primo=False
     return 0,primo
  if suma==1:
     primo=True
     return suma ,primo  
  else:
     primo=False
     return suma,primo