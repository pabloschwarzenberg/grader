#Suma de los N primeros números
def calcular_suma_naturales(n):
    suma = n * (n + 1) // 2
    print("La suma de los", n, "primeros números naturales es:", suma)

# Solicitar el número al usuario
N = int(input("Ingrese un número entero positivo: "))

# Llamar a la función para calcular e imprimir la suma
calcular_suma_naturales(N)      