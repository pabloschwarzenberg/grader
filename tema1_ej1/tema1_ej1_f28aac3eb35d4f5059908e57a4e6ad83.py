def suma_primeros_naturales(n):
    suma = n * (n + 1) // 2  # Calcula la suma de los primeros n números naturales
    return suma

# Solicitar al usuario ingresar el número N
N = int(input("Ingrese el valor de N: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_primeros_naturales(N)

# Imprimir el resultado
print("La suma de los", N, "primeros números naturales es:", resultado)