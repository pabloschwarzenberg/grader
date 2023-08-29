#Suma de los N primeros números
def suma_naturales(n):
    suma = n * (n + 1) // 2
    return suma

# Solicitar al usuario ingresar un número N
N = int(input("Ingrese un número: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_naturales(N)

# Imprimir el resultado
print("La suma de los", N, "primeros números naturales es:", resultado)   