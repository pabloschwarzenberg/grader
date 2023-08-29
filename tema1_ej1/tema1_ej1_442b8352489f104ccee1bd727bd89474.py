def suma_n_primeros_numeros(n):
    suma = n * (n + 1) // 2
    return suma
#____________________________________________
N = int(input("Ingrese un número N: "))
resultado = suma_n_primeros_numeros(N)
print("La suma de los primeros", N, "números naturales es:", resultado)