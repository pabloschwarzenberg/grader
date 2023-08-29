def suma_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

# Solicitar al usuario el número N
numero = int(input("Ingresa un número entero positivo: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_naturales(numero)

# Imprimir el resultado
print("La suma de los", numero, "primeros números naturales es:", resultado)
