#Suma de los N primeros números
n=int(input("Ingrese la cantidad de números naturales a sumar "))
while(n<=0):
    n=int(input("Ingrese la cantidad de números naturales a sumar "))
suma=((n+1)*n)/2
print(suma)