#Suma de los N primeros números
def calcular_suma_naturales(N):
    suma = N * (N + 1) // 2
    print("La suma de los", N, "primeros números naturales es:", suma)

# Pedir al usuario que ingrese el valor de N
N = int(input("Ingrese un número entero positivo: "))

# Llamar a la función para calcular e imprimir la suma de los N primeros números naturales
calcular_suma_naturales(N)
