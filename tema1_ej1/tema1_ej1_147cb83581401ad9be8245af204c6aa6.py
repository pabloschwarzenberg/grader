def suma_n_primeros_numeros(n):
    suma = n * (n + 1) // 2
    return suma

numero = int(input("Ingrese un número: "))

resultado = suma_n_primeros_numeros(numero)
print("La suma de los primeros", numero, "números naturales es:", resultado)
