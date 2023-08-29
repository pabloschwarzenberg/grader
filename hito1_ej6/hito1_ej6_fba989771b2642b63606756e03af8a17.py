#Ordenar tres número
a = int(input("ingrese numero "))
m = int(input("ingrese numero "))
t = int(input("ingrese numero "))
if a>m:
  aux = a ; a=m ; m = aux
if a>t :
  aux = a ; a=t ; t = aux
if m>t :
  aux = m ; m=t ; t = aux
print (a,",",m,",",t)