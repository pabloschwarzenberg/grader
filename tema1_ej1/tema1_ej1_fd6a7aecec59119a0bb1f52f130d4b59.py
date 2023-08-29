#Suma de los N primeros números
def suma_numeros_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

# Solicitar el número N al usuario
N = int(input("Ingrese un número entero positivo: "))

# Validar que el número sea positivo
if N <= 0:
    print("El número debe ser positivo.")
else:
    # Calcular la suma de los N primeros números naturales
    resultado = suma_numeros_naturales(N)
    print("La suma de los", N, "primeros números naturales es:", resultado)
   