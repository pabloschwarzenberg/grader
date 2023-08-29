#Suma de los N primeros números
def suma_numeros_naturales(N):
    suma = N * (N + 1) // 2
    return suma

# Solicitar el número N al usuario
N = int(input("Ingrese el valor de N: "))

# Calcular la suma de los primeros N números naturales
resultado = suma_numeros_naturales(N)

# Imprimir el resultado
print("La suma de los primeros", N, "números naturales es:", resultado)
      