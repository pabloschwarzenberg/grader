#Suma de los N primeros números
N = int(input("Ingresa un número N: "))
suma = 0

for i in range(1, N + 1):
    suma += i

print("La suma de los", N, "primeros números naturales es:", suma)