def suma_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma


numero = int(input("Ingrese un número entero positivo: "))

# Calcular y mostrar la suma de los N primeros números naturales
resultado = suma_naturales(numero)
print("La suma de los", numero, "primeros números naturales es:", resultado)