#Listas
primos=[]
divisores=[]
time=0
#Variable
nd=int(input("Ingrese numero a descomponer --> "))
#Funcion verificadora de primos
def p(x):
  if x<2:
    return False
  for l in range (2,x):
    if x % l == 0:
      return False
  return True
#Descomponer
if nd<2:
  print("Tu numero no tiene descomposición en primos, (es menor a 2")

elif p(nd)== True:
  print(nd)

elif p(nd)== False:
  for pr in range (2,nd):
   if p(pr)== True:
     primos.append(pr)
  while nd > 0 and time<100:
   for d in (primos):
     if nd % d == 0:
       nd=nd/d 
       print (d)
       divisores.append(d)
       break
   time=time+1
  
  