def suma_n_primeros_numeros(n):
    suma = n * (n + 1) // 2
    return suma

# Obtener el número N del usuario
N = int(input("Ingrese un número entero positivo: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_n_primeros_numeros(N)

# Imprimir el resultado
print("La suma de los primeros", N, "números naturales es:", resultado)