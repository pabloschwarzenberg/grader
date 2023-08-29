def suma_n_primeros_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

# Solicitar el número al usuario
N = int(input("Ingrese un número entero positivo: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_n_primeros_naturales(N)

# Imprimir el resultado
print("La suma de los", N, "primeros números naturales es:", resultado)

      