#Suma de los N primeros números
def suma_primeros_n_numeros(n):
    suma = n * (n + 1) // 2
    return suma

# Pedimos al usuario que ingrese el número N
numero = int(input("Ingrese un número entero positivo: "))

# Calculamos la suma de los primeros N números naturales
resultado = suma_primeros_n_numeros(numero)

# Imprimimos el resultado
print("La suma de los primeros", numero, "números naturales es:", resultado)