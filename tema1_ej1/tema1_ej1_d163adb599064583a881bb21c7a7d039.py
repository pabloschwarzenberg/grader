def suma_n_primeros_numeros(n):
    suma = n * (n + 1) // 2
    return suma

# Solicitar al usuario el número N
numero_n = int(input("Ingresa un número N: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_n_primeros_numeros(numero_n)

# Imprimir el resultado
print("La suma de los", numero_n, "primeros números naturales es:", resultado)
