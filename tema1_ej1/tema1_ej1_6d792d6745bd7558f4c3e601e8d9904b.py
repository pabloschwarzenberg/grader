#Suma de los N primeros números
 def calcular_suma_naturales(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma


N = int(input("Ingrese un número entero positivo N: "))


suma_naturales = calcular_suma_naturales(N)


print("La suma de los", N, "primeros números naturales es:", suma_naturales)

