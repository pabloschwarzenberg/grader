# Suma de los N primeros números

def suma_n_primeros_numeros(n):
    suma = n * (n + 1) // 2
    return suma

# Solicitar al usuario que ingrese el valor de N
N = int(input("Ingrese un número N: "))

# Calcular la suma de los N primeros números
resultado = suma_n_primeros_numeros(N)

# Imprimir el resultado
print("La suma de los", N, "primeros números naturales es:", resultado)
