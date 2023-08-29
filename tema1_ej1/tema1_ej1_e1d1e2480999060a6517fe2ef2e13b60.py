def primeros_numeros(n):
    suma = n * (n + 1) / 2
    return suma

n = int(input("Ingresa un número: "))
print("La suma de los primeros", n, "números naturales es:", primeros_numeros(n))