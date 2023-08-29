def suma_n_primeros_numeros(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

numero = int(input("Ingrese un número entero positivo: "))

resultado = suma_n_primeros_numeros(numero)

print("La suma de los", numero, "primeros números naturales es:", resultado)
