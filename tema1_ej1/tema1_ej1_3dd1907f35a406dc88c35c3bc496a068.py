def suma_n_primeros(n):
    suma = n * (n + 1) // 2
    return suma

num = int(input("Introduce un número entero positivo: "))
suma = suma_n_primeros(num)
print("La suma de los primeros", num, "números naturales es:", suma)
