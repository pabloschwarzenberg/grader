def suma_naturales(n):
    suma = n * (n + 1) // 2
    return suma

numero = int(input("Ingresa un número: "))
resultado = suma_naturales(numero)
print("La suma de los primeros", numero, "números naturales es:", resultado)