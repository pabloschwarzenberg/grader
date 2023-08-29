def suma_n_primeros_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma
numero = int(input("Ingrese un número: "))
suma = suma_n_primeros_naturales(numero)
print("La suma de los", numero, "primeros números naturales es:", suma)      