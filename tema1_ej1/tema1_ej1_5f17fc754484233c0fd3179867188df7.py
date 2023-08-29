def suma_n_primeros_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

# Solicitamos al usuario que ingrese el valor de N
N = int(input("Ingrese un número entero positivo: "))

# Verificamos si el número ingresado es válido
if N <= 0:
    print("El número ingresado debe ser positivo.")
else:
    # Calculamos la suma de los N primeros números naturales
    resultado = suma_n_primeros_naturales(N)
    print("La suma de los", N, "primeros números naturales es:", resultado)
