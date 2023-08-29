def suma_numeros_naturales(n):
    suma = n * (n + 1) // 2
    return suma

numero = int(input("Ingrese un número N: "))


resultado = suma_numeros_naturales(numero)
print("La suma de los", numero, "primeros números naturales es:", resultado)