#Suma de los N primeros números
n = int(input("ingrese N: "))
          
suma = n * (n + 1)/2

print(suma) 

suma = 0
for i in range (1, n + 1):
    suma += i

print(suma)


suma = sum(range(1, n +1))

print(suma)     