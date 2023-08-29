#Suma de los N primeros números
def calcular_suma_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

# Solicitar el número al usuario
N = int(input("Ingrese un número entero: "))

# Verificar si el número es positivo
if N < 0:
    print("El número debe ser positivo.")
else:
    # Calcular la suma de los primeros N números naturales
    suma_naturales = calcular_suma_naturales(N)

    # Imprimir la suma calculada
    print("La suma de los primeros", N, "números naturales es:", suma_naturales)
