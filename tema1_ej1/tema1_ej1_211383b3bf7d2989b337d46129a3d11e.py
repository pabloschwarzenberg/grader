def suma_naturales(N):
    suma = N * (N + 1) // 2
    return suma

# Solicitar el valor de N al usuario
N = int(input("Ingrese el valor de N: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_naturales(N)

# Imprimir el resultado
print("La suma de los primeros", N, "números naturales es:", resultado)

      