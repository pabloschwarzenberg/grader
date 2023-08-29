def suma_n_primeros_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma


# Solicitar al usuario el valor de N
numero = int(input("Ingrese un número entero positivo: "))

# Calcular la suma de los primeros N números naturales
resultado = suma_n_primeros_naturales(numero)

# Imprimir el resultado
print("La suma de los primeros", numero, "números naturales es:", resultado)