def suma_naturales(n):
    return n * (n + 1) // 2

N = int(input("Ingrese un número entero positivo: "))
print("La suma de los primeros", N, "números naturales es:", suma_naturales(N))