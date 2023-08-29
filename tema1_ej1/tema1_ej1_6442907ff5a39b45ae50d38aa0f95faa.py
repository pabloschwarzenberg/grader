def suma_n_primeros_numeros(n):
    suma = (n * (n + 1)) // 2
    return suma

N = int(input("Ingrese un número entero positivo: "))

suma_total = suma_n_primeros_numeros(N)

print("La suma de los", N, "primeros números naturales es:", suma_total)