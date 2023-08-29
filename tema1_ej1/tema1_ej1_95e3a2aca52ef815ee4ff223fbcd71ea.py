#Suma de los N primeros números
n=int(input("ingrese un número N"))
if n/2==0:
    suma=(n*(n/2))+(n/2)
    print(suma)
else:
    suma=n*((n//2)+1)
    print(suma)