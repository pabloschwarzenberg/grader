def suma_numeros_naturales(N):
    suma = N * (N + 1) // 2
    print("La suma de los", N, "primeros números naturales es:", suma)

# Ejemplo de uso
N = int(input("Ingrese un número entero positivo: "))

suma_numeros_naturales(N)
