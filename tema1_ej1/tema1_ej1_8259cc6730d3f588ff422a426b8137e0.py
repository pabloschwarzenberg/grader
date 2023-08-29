#Suma de los N primeros números
n=int(input("Ingrese un número: "))
m=((n*(n+1))/2)
if n==1:
    print("La suma del primer número natural es:",1)
else:
    print("La suma de los primeros",n,"números naturales es:",m)     