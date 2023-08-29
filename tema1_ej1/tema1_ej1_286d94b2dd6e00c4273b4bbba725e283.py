#Suma de los N primeros números
def suma_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

# Pedir al usuario que ingrese el número N
n = int(input("Ingrese un número entero positivo: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_naturales(n)

# Imprimir la suma
print("La suma de los primeros {} números naturales es: {}".format(n, resultado))