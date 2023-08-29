def calcular_suma_primeros_n(n):
    suma = n * (n + 1) // 2
    return suma

numero = int(input("Ingrese un número entero positivo: "))
suma_total = calcular_suma_primeros_n(numero)
print("La suma de los", numero, "primeros números naturales es:", suma_total)
