#Suma de los N primeros números naturales
def suma_n_primeros_numeros(n):
    suma = n * (n + 1) // 2
    return suma

# Obtener el número N del usuario
N = int(input("Ingrese un número entero positivo: "))

# Verificar que el número ingresado sea válido
if N <= 0:
    print("El número debe ser un entero positivo.")
else:
    # Calcular la suma de los N primeros números naturales
    resultado = suma_n_primeros_numeros(N)
    print("La suma de los", N, "primeros números naturales es:", resultado)

      