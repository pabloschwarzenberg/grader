#Suma de los N primeros números
def suma_naturales(n):
    suma = n * (n + 1) // 2
    return suma

# Obtener el número N del usuario
N = int(input("Ingresa un número entero positivo: "))

# Calcular la suma de los N primeros números naturales
suma_total = suma_naturales(N)

# Imprimir la suma
print("La suma de los", N, "primeros números naturales es:", suma_total)