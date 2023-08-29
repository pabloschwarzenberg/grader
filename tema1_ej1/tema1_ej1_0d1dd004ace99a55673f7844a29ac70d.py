#Suma de los N primeros números
def suma_naturales(n):
    suma = n * (n + 1) // 2
    return suma

# Pedir al usuario que ingrese el valor de N
N = int(input("Ingrese el valor de N: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_naturales(N)

# Imprimir el resultado
print("La suma de los", N, "primeros números naturales es:", resultado)
