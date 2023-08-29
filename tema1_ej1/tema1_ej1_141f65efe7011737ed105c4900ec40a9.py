#Suma de los N primeros números
n=int(input("Ingrese un número"))
suma=n*(n+1)/2
print(suma)
print()
suma=0
for i in range(1,n+1):
    suma+=i
print(suma)
print()
suma=sum(range(1,n+1))
print(suma)