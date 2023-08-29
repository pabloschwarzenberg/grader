# Factores Primos
def factorizar_primos(numero):
    # Verificar si el número es negativo o cero
    if numero <= 0:
        print("Ingresa un número entero positivo.")
        return

    # Encontrar los factores primos
    factor = 2
    while factor * factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero //= factor
        else:
            factor += 1

    if numero > 1:
        print(numero)

# Solicitar al usuario que ingrese un número entero
numero = int(input())

# Llamar a la función para factorizar los primos y mostrar los resultados
factorizar_primos(numero)
