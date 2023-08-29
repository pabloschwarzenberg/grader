def suma_n_primeros_numeros(n):
    suma = (n * (n + 1)) // 2  # Aplica la fórmula de la suma de los primeros n números naturales
    return suma


# Solicita al usuario ingresar un número entero N
N = int(input("Ingrese un número entero N: "))

# Calcula la suma de los N primeros números naturales
resultado = suma_n_primeros_numeros(N)

# Imprime el resultado
print("La suma de los", N, "primeros números naturales es:", resultado)

      