#Suma de los N primeros números
def suma_n_primeros_numeros(n):
    suma = (n * (n + 1)) // 2
    return suma

# Solicitar al usuario ingresar el valor de N
N = int(input("Ingresa el valor de N: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_n_primeros_numeros(N)

# Mostrar el resultado
print("La suma de los", N, "primeros números naturales es:", resultado)
