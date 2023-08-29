def suma_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

# Solicitamos al usuario ingresar el valor de N
N = int(input("Ingrese el valor de N: "))

# Calculamos la suma de los N primeros números naturales
resultado = suma_naturales(N)

# Imprimimos el resultado
print("La suma de los", N, "primeros números naturales es:", resultado)
