# completa el código de la función
def amigos(a,b):
  sumaa=0
  sumab=0
 
  for i in range (1,a):
    if a%i==0:
      sumaa = sumaa + i
    
  for j in ranje (1,b):
    if b%i==0:
      sumab = sumab + j 
  
  return sumaa==b and sumab==a

a=input("")
b=input("")
a=int(a)
b=int(b)

if amigos(a,b):
  print (True)
else:
  print(False)