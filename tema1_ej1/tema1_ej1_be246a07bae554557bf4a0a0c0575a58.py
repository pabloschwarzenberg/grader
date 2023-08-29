def suma_n_primeros_numeros(n):
    suma = n * (n + 1) // 2
    return suma

# Solicitar el número al usuario
numero = int(input("Ingresa un número: "))

# Calcular e imprimir la suma de los primeros números naturales
resultado = suma_n_primeros_numeros(numero)
print("La suma de los primeros", numero, "números naturales es:", resultado)   