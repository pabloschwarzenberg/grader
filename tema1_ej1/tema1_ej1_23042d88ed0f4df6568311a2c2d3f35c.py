#Suma de los N primeros números
def suma_naturales(n):
    suma = n * (n + 1) // 2
    return suma

N = int(input("Ingrese el número N: "))

resultado = suma_naturales(N)

print("La suma de los primeros", N, "números naturales es:", resultado)
