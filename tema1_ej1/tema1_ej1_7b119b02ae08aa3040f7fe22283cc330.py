#Suma de los N primeros números
n = int(input("Ingrese el valor de N: "))
suma = 0
for i in range(1, n + 1):
    suma += i
print("La suma de los primeros", n, "números naturales es:", suma)     