#Suma de los N primeros números
n=int(input("Ingrese un numero:"))
while n<0:
    print("Ingrese un numero positivo:")
    n=int(input())
else:
    suma=(n*(n+1))/2
    print("La sumatoria es:",suma)
