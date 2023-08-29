def suma_primeros_n_numeros(n):
    # Calcula la suma de los primeros n números naturales utilizando la fórmula n(n + 1)/2
    suma = n * (n + 1) // 2
    return suma

# Solicita al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Calcula la suma de los primeros n números naturales llamando a la función suma_primeros_n_numeros
resultado = suma_primeros_n_numeros(numero)

# Imprime el resultado de la suma de los primeros n números naturales
print("La suma de los", numero, "primeros números naturales es:", resultado)
