# completa el código de la función
def suma_divisores(a):
  suma_divisores=0
  for i in range(1,a):
   if a%i==0:
       suma_divisores+=i
  if a==1:
          return(0,False)
  if suma_divisores==1:
     return(suma_divisores,True)
  elif suma_divisores>1:
     return(suma_divisores,False)
for i in range(0,30):
    print(suma_divisores(i))

   
           