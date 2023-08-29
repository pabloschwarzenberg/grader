def suma_primeros_n_numeros(n):
    suma = n * (n + 1) // 2
    return suma

# Obtener el número N desde el usuario
N = int(input("Ingrese un número entero positivo: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_primeros_n_numeros(N)

# Imprimir el resultado
print("La suma de los", N, "primeros números naturales es:", resultado)