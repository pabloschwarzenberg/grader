#Suma de los N primeros números
def suma_numeros_naturales(n):
    suma = (n * (n + 1)) // 2
    print("La suma de los", n, "primeros números naturales es:", suma)

# Solicitar el valor de N al usuario
N = int(input("Ingrese un número entero positivo: "))

# Verificar si el número ingresado es válido
if N <= 0:
    print("El número ingresado no es válido. Debe ser un entero positivo.")
else:
    # Llamar a la función para calcular y mostrar la suma
    suma_numeros_naturales(N)