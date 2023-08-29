#Suma de los N primeros números
def suma_n_primeros(n):
    suma = n * (n + 1) // 2
    return suma

# Pedimos al usuario que ingrese el número N
N = int(input("Ingrese un número entero positivo: "))

# Calculamos la suma de los N primeros números naturales
resultado = suma_n_primeros(N)

# Imprimimos el resultado
print("La suma de los", N, "primeros números naturales es:", resultado)
  