#Suma de los N primeros números
def suma_numeros_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

# Obtener el número N del usuario
N = int(input("Ingrese un número N: "))

# Calcular la suma de los N primeros números naturales
suma_total = suma_numeros_naturales(N)

# Imprimir el resultado
print("La suma de los", N, "primeros números naturales es:", suma_total)
