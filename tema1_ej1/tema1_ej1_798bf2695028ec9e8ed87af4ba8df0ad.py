#Suma de los N primeros números
def suma(n):
    suma = n * (n + 1) / 2
    return suma

N = int(input("Ingresa un número: "))
resultado = suma(N)
print("La suma de los primeros", N, "números naturales es:", resultado)