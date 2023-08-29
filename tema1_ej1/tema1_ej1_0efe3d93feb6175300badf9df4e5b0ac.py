from os import system
system ("cls")
def suma_naturales(n):
    suma = n * (n + 1) // 2
    print("La suma de los primeros", n, "números naturales es:", suma)

# Ejemplo de uso
N = int(input("Ingrese un número N: "))
suma_naturales(N)

      