def suma_numeros_naturales(n):
    suma = n * (n + 1) // 2
    return suma

# Pedir al usuario que ingrese el valor de N
numero_n = int(input("Ingrese el valor de N: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_numeros_naturales(numero_n)

# Imprimir el resultado
print("La suma de los primeros", numero_n, "números naturales es:", resultado)
