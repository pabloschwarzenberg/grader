#Suma de los N primeros números
def calcular_suma_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

# Solicitar número al usuario
N = int(input("Ingresa un número entero positivo: "))

# Verificar que el número sea positivo
if N < 0:
    print("El número debe ser positivo.")
else:
    # Calcular la suma de los N primeros números naturales
    suma_naturales = calcular_suma_naturales(N)
    print("La suma de los primeros", N, "números naturales es:", suma_naturales)
      