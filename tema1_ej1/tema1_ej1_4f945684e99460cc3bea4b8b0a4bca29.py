#Suma de los N primeros números
n = int(input("ingrese un numero:"))
suma = n * (n + 1)/2

print(suma)
print()

suma = 0
for i in range(1, n + 1):
    suma = 0
print (suma)
print()

suma = sum(range(1, n +1))
print(suma)