#Suma de los N primeros números
N = int(input("Ingrese un número entero positivo: "))

# Validar que el número sea positivo
if N <= 0:
    print("El número debe ser positivo.")
else:
    # Calcular la suma de los N primeros números naturales
    suma = N * (N + 1) // 2

    # Imprimir la suma
    print("La suma de los", N, "primeros números naturales es:", suma)
