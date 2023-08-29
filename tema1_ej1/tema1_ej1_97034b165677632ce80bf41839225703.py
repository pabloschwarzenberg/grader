#Suma de los N primeros números
def suma_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma


# Solicitar al usuario que ingrese el número N
numero_N = int(input("Ingrese el número N: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_naturales(numero_N)

# Imprimir el resultado
print("La suma de los", numero_N, "primeros números naturales es:", resultado)
