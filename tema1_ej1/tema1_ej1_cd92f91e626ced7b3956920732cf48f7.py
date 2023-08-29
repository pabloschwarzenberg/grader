#Suma de los N primeros números
def calcular_suma_naturales(n):
    suma = n * (n + 1) // 2
    return suma


# Solicitar al usuario que ingrese el número N
numero_n = int(input("Ingrese el número N: "))

# Calcular la suma de los N primeros números naturales
suma_total = calcular_suma_naturales(numero_n)

# Imprimir el resultado
print("La suma de los primeros", numero_n, "números naturales es:", suma_total)
