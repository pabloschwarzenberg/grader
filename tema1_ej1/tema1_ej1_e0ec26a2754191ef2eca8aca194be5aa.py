#Suma de los N primeros números
def suma_n_primeros_naturales(n):
    suma = n * (n + 1) // 2
    return suma

# Solicitar al usuario el número N
N = int(input("Ingrese un número entero positivo: "))

# Verificar que el número ingresado sea válido
if N <= 0:
    print("El número ingresado debe ser un entero positivo.")
else:
    # Calcular la suma de los N primeros números naturales
    suma_n = suma_n_primeros_naturales(N)

    # Imprimir el resultado
    print("La suma de los", N, "primeros números naturales es:", suma_n)