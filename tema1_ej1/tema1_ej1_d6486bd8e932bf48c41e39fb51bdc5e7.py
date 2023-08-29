#Suma de los N primeros números
N = int(input("Ingresa un número entero positivo: "))
if N <= 0:
    print("El número ingresado debe ser un entero positivo.")
else:
    suma = N * (N + 1) // 2
    print("La suma de los", N, "primeros números naturales es:", suma)
