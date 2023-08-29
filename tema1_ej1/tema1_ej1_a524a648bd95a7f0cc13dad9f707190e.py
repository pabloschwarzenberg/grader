def suma_numeros_naturales(n):
    suma = n * (n + 1) // 2
    return suma

numero = int(input("Ingrese un número entero positivo: "))

suma_total = suma_numeros_naturales(numero)

print("La suma de los primeros", numero, "números naturales es:", suma_total)

      