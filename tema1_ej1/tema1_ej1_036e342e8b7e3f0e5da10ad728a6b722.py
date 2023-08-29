def suma_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

# Solicitar el número N al usuario
N = int(input("Ingrese el valor de N: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_naturales(N)

# Imprimir el resultado
print("La suma de los", N, "primeros números naturales es:", resultado)