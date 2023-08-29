#Suma de los N primeros números
def suma_numeros_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

# Ingrese el valor de N
N = int(input("Ingresa un número entero N: "))

# Calcular la suma de los primeros N números naturales
suma_total = suma_numeros_naturales(N)

print("La suma de los primeros", N, "números naturales es:", suma_total)
