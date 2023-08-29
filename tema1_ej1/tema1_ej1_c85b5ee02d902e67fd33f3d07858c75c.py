def suma_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

N = int(input("Ingrese un número entero: "))

suma_total = suma_naturales(N)

print("La suma de los", N, "primeros números naturales es:", suma_total)

      