def suma_n_primeros_numeros(n):
    suma = (n * (n + 1)) // 2
    return suma

# Solicitar el número al usuario
numero = int(input("Ingrese un número entero positivo: "))

# Validar que el número sea positivo
if numero <= 0:
    print("El número debe ser positivo.")
else:
    # Calcular la suma de los primeros números naturales
    resultado = suma_n_primeros_numeros(numero)
    print("La suma de los primeros", numero, "números naturales es:", resultado)