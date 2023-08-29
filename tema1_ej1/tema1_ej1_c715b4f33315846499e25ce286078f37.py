def suma_n_primeros_numeros(n):
    suma = n * (n + 1) // 2
    return suma

# Solicitar el valor de N al usuario
N = int(input("Ingrese el valor de N: "))

# Calcular la suma de los primeros N números naturales
resultado = suma_n_primeros_numeros(N)

# Imprimir el resultado
print("La suma de los primeros", N, "números naturales es:", resultado)