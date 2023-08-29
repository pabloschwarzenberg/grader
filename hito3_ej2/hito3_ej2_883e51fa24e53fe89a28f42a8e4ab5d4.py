def calcular_suma_n_primeros_naturales(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

N = int(input("Ingresa el valor de N: "))

suma_total = calcular_suma_n_primeros_naturales(N)

print("La suma de los primeros", N, "números naturales es:", suma_total)