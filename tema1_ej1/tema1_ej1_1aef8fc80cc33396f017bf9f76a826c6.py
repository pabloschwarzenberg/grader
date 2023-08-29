def suma_n_primeros_numeros(n):
    suma = (n * (n + 1)) // 2
    return suma

#recopilacion de datos(usuario)
N = int(input("Ingrese un número entero positivo: "))

#cálculo
suma_total = suma_n_primeros_numeros(N)

#salida
print("La suma de los", N, "primeros números naturales es:", suma_total)
