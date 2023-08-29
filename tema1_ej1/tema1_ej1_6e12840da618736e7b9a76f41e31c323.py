def suma_n_primeros_numeros(n):
    suma = (n * (n + 1)) // 2
    return suma

# Solicitar al usuario el número N
N = int(input("Ingrese un número N: "))

# Calcular la suma de los N primeros números naturales
suma = suma_n_primeros_numeros(N)

# Imprimir la suma
print("La suma de los", N, "primeros números naturales es:", suma)
