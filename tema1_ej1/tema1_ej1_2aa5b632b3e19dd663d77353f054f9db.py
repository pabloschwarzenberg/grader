def suma_n_primeros_naturales(N):
    suma = (N * (N + 1)) // 2
    return suma

# Solicitar al usuario ingresar el número N
N = int(input("Ingrese el valor de N: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_n_primeros_naturales(N)

# Imprimir el resultado
print("La suma de los", N, "primeros números naturales es:", resultado)
