def calcular_suma_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

# Ejemplo de uso
numero_n = int(input("Ingresa un número entero N: "))

suma_total = calcular_suma_naturales(numero_n)
print("La suma de los primeros", numero_n, "números naturales es:", suma_total)

      