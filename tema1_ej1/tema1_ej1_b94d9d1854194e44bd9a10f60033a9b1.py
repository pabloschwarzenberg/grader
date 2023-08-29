def suma_n_primeros_numeros(n):
    suma = n * (n + 1) // 2
    return suma

# Solicitar el número N al usuario
N = int(input("Ingrese un número entero positivo: "))

# Verificar que el número sea válido
if N < 1:
    print("El número debe ser positivo.")
else:
    # Calcular la suma de los N primeros números naturales
    suma_total = suma_n_primeros_numeros(N)
    print("La suma de los", N, "primeros números naturales es:", suma_total)

      