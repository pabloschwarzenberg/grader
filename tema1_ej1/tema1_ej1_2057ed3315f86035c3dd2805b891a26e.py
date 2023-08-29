N = int(input("Ingrese un número entero positivo: "))

# Verificamos que N sea un número positivo
if N < 1:
    print("El número debe ser positivo.")
else:
    # Inicializamos la variable de suma
    suma = 0

    # Iteramos desde 1 hasta N (incluyendo N)
    for i in range(1, N + 1):
        suma += i  # Agregamos el valor actual a la suma

    # Imprimimos el resultado
    print("La suma de los", N, "primeros números naturales es:", suma)