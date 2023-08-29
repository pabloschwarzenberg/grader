def suma_n_primeros_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

# Solicitar el número al usuario
numero = int(input("Ingrese un número: "))

# Llamar a la función y mostrar el resultado
resultado = suma_n_primeros_naturales(numero)
print("La suma de los", numero, "primeros números naturales es:", resultado)
