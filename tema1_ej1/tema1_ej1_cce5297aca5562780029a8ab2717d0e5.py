def suma_naturales(N):
    suma = N * (N + 1) // 2
    return suma

# Solicitar el número N al usuario
N = int(input("Ingrese un número entero positivo: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_naturales(N)

# Imprimir el resultado
print("La suma de los", N, "primeros números naturales es:", resultado)