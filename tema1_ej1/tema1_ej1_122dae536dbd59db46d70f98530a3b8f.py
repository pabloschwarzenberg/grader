#Suma de los N primeros números
# Solicitar el número N al usuario
numero_n = int(input("Ingrese el valor de N: "))

# Calcular la suma de los N primeros números naturales
def calcular_suma_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma
suma_naturales = calcular_suma_naturales(numero_n)

# Mostrar el resultado
print("La suma de los", numero_n, "primeros números naturales es:", suma_naturales)

      