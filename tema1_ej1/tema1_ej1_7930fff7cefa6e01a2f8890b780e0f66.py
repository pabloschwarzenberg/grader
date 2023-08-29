def suma_n_primeros_numeros(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

N = int(input("Ingrese el valor de N: "))

resultado = suma_n_primeros_numeros(N)

print("La suma de los", N, "primeros números naturales es:", resultado)