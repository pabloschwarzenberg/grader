#Suma de los N primeros números
def suma_naturales(n):
    suma = n * (n + 1) // 2
    return suma

# Solicitar al usuario ingresar el número N
numero_N = int(input("Ingrese un número N: "))

# Calcular la suma de los primeros N números naturales
resultado = suma_naturales(numero_N)

# Imprimir el resultado
print("La suma de los primeros", numero_N, "números naturales es:", resultado)