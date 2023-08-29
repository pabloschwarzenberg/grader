def suma_primeros_n_numeros(n):
    suma = (n * (n + 1)) // 2
    return suma
N = int(input("Ingrese un número entero positivo N: "))
resultado = suma_primeros_n_numeros(N)
print("La suma de los", N, "primeros números naturales es:", resultado)