def suma_n_primeros_numeros(n):
    suma = (n * (n + 1)) / 2
    return int(suma)

n = int(input("Ingrese un número N: "))
resultado = suma_n_primeros_numeros(n)
print("La suma de los", n, "primeros números naturales es:", resultado)