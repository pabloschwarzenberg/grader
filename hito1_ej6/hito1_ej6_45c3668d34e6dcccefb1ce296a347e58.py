#Ordenar tres números
lista=list()
for x in range(3):
    x=int(input("ingrese un numero cualquiera:"))
    lista.append(x)
  
lista.sort()
r=""
for n in range(3):
  if n<2:
    r=r+str(lista[n]) + ","
  if  n==2:
    r=r+str(lista[n])
 
print(r)