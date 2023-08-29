#Suma de los N primeros números
def suma_numeros_naturales(n):
    suma = n * (n + 1) // 2
    return suma
# Solicitar el número N al usuario
N = int(input("Ingrese un número entero positivo: "))
# Validar que el número ingresado sea positivo
if N < 0:
    print("El número ingresado no es válido. Debe ser un entero positivo.")
else:
    # Calcular la suma de los N primeros números naturales
    suma_total = suma_numeros_naturales(N)  
    # Imprimir la suma
    print("La suma de los", N, "primeros números naturales es:", suma_total) 