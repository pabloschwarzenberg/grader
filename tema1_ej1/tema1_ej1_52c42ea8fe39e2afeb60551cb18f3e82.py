def suma_naturales(n):
    suma = n * (n + 1) // 2
    return suma

# Solicitar el número N al usuario
n = int(input("Ingrese un número entero positivo: "))

# Validar que el número sea positivo
if n < 1:
    print("El número debe ser mayor o igual a 1.")
else:
    # Calcular la suma de los N primeros números naturales
    resultado = suma_naturales(n)

    # Imprimir el resultado
    print("La suma de los", n, "primeros números naturales es:", resultado)
