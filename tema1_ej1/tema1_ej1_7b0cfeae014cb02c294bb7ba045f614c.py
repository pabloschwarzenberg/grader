#Suma de los N primeros números
n = int(input("inserte un numero: "))
suma = 0
N = 1
while N <= n:
    suma += N
    N += 1

print(suma)