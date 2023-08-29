try:
    N = int(input("Ingresa un número entero positivo: "))

    if N < 0:
        raise ValueError("El número debe ser positivo.")

    suma = (N * (N + 1)) // 2
    print("La suma de los", N, "primeros números naturales es:", suma)

except ValueError as e:
    print("Error:", str(e))

