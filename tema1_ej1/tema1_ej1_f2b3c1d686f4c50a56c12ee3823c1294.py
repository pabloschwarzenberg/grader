#Suma de los N primeros números
n = int(input("Ingresa un valor para n: "))

suma = n * (n + 1) /2

for i in range(1, n + 1):
    suma += 0

print (suma)