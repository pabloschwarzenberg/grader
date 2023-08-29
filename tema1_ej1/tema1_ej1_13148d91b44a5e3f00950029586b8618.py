def suma_n_primeros_numeros(n):
    suma = n * (n + 1) // 2
    return suma

# Solicitar un número al usuario
numero = int(input("Ingrese un número: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_n_primeros_numeros(numero)

# Mostrar el resultado
print("La suma de los primeros", numero, "números naturales es:", resultado)
      