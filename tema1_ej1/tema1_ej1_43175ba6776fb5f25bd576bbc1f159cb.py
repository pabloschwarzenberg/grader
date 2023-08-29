def suma_naturales(N):
    suma = N * (N + 1) // 2
    return suma

# Pedir al usuario que ingrese el número N
N = int(input("Ingrese el valor de N: "))
resultado=0
# Calcular la suma de los N primeros números naturales
resultado = suma_naturales(N)
# Imprimir el resultado
print("La suma de los", N, "primeros números naturales es:", resultado)