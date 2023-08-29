def suma_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

# Entrada
N = int(input("Ingrese el número N: "))

# Cálculo
resultado = suma_naturales(N)

# Salida
print("La suma de los {} primeros números naturales es: {}".format(N, resultado))
