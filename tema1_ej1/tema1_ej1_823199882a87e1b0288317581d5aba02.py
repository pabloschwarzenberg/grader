def suma_numeros_naturales(n):
    suma = (n * (n + 1)) // 2
    print("La suma de los", n, "primeros números naturales es:", suma)

# Pedir al usuario que ingrese el número N
numero = int(input("Ingrese un número entero N: "))

# Llamar a la función para calcular e imprimir la suma de los N primeros números naturales
suma_numeros_naturales(numero)
