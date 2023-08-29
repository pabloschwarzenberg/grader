#Suma de los N primeros números
def suma_n_primeros_naturales(n):
    suma = n * (n + 1) // 2
    return suma

# Solicitar al usuario el número N
numero_N = int(input("Ingresa un número entero positivo: "))

# Calcular la suma de los N primeros números naturales
suma_naturales = suma_n_primeros_naturales(numero_N)

# Imprimir el resultado
print("La suma de los primeros", numero_N, "números naturales es:", suma_naturales)
    