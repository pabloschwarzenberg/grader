#Suma de los N primeros números

N = int(input('Ingrese el numero N: '))
i = 1

while i < N:
    n = N * (N + 1) / 2
    i += 1

print(n)