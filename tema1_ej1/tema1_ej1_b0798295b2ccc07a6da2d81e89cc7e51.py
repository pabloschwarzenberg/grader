def suma_naturales(n):
    suma = n * (n + 1) // 2
    return suma

# Ejemplo de uso
N = int(input("Ingrese un número: "))

resultado = suma_naturales(N)
print("La suma de los primeros", N, "números naturales es:", resultado)
