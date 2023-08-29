#Suma de los N primeros números
def suma_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

# Pedir al usuario que ingrese el valor de N
N = int(input("Ingrese un número entero positivo: "))

# Calcular la suma de los primeros N números naturales
resultado = suma_naturales(N)

# Imprimir el resultado
print("La suma de los primeros", N, "números naturales es:", resultado)