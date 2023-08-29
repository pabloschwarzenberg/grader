#Suma de los N primeros números
def calcular_suma_naturales(n):
    suma = n * (n + 1) // 2
    return suma

# Pedir al usuario que ingrese un número
N = int(input("Ingrese un número entero positivo: "))

# Validar que el número ingresado sea positivo
if N < 0:
    print("El número ingresado debe ser positivo.")
else:
    # Calcular la suma de los N primeros números naturales
    suma_naturales = calcular_suma_naturales(N)

    # Imprimir el resultado
    print("La suma de los", N, "primeros números naturales es:", suma_naturales)
