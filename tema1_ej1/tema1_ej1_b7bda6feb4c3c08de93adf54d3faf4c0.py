def calcular_suma_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

N = int(input("Ingrese el valor de N: "))

suma_total = calcular_suma_naturales(N)
print("La suma de los primeros", N, "números naturales es:", suma_total)