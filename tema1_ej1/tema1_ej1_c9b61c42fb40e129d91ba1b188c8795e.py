#Suma de los N primeros números
N = int(input("Ingrese un numero: "))
while not(N>0):
    N = int(input("Error!Ingrese otro valor: "))
Suma = N*(N+1)/2
print("La suma es: ",Suma)      