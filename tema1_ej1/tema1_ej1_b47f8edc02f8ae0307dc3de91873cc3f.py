#Suma de los N primeros números
def suma_n_primeros_naturales(n):
    suma = (n * (n + 1)) / 2
    return int(suma)

# Solicitar el número al usuario
N = int(input("Ingrese un número entero positivo: "))

# Calcular la suma de los primeros N números naturales
resultado = suma_n_primeros_naturales(N)

# Mostrar el resultado
print("La suma de los primeros", N, "números naturales es:", resultado)    