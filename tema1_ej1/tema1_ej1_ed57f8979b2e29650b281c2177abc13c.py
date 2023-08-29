def suma_n_primeros_numeros(n):
    suma = (n * (n + 1)) // 2
    return suma

# Ejemplo de uso
numero = int(input("Ingresa un número entero positivo: "))

if numero < 1:
    print("El número debe ser positivo.")
else:
    resultado = suma_n_primeros_numeros(numero)
    print("La suma de los primeros", numero, "números naturales es:", resultado)
