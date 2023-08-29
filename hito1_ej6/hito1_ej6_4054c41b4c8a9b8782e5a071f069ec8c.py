#Ordenar tres números
a= int(input("ingrese el valor de a ",))
b= int(input("Ingrese el valor de b ",))
c= int(input("Ingrese el valor de c ",))
if a > b:
  aux = a ; a = b ; b = aux
if a > c :
  aux = a ;a = c ; c = aux
if b > c :
  aux = b ; b = c ; c = aux
print ( a,",",b,",",c)