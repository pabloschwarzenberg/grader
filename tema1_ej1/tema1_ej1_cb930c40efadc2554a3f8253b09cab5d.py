#Suma de los N primeros números
N=int(input("Ingrese un valor N para la suma de los primeros numeros naturales: "))
if N>0:
    sum=N*(N+1)//2
    print("La suma de los N primeros numeros naturales es: ",sum)
else:
    print("Ingrese un valor valido porfavor: ")