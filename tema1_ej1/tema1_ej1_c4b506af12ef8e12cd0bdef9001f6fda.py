n = int(input("Ingrese un número para encontrar la sumatoria de los naturales hasta el numero indicado: "))

"""solucion usando ciclos
suma = 0
for i in range(1,n+1):
    suma += i
print("La suma de los ",n," primeros numeros naturales es: ",suma) """

suma = int((n * (n + 1)) / 2)
print("La suma de los ",n," primeros numeros naturales es: ",suma)