def suma_numeros_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

# Solicitar el número N al usuario
numero = int(input("Ingrese un número: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_numeros_naturales(numero)

# Imprimir el resultado
print("La suma de los", numero, "primeros números naturales es:", resultado)