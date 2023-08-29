#Suma de los N primeros números
def calcular_suma_naturales(n):
    suma = n * (n + 1) // 2
    return suma

# Solicitar el número N al usuario
numero_N = int(input("Ingresa un número entero positivo N: "))

# Calcular la suma de los N primeros números naturales
suma_total = calcular_suma_naturales(numero_N)

# Mostrar el resultado
print("La suma de los", numero_N, "primeros números naturales es:", suma_total)
      