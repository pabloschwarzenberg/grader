#Factores Primos
def factorizar_primos(numero):
    # Inicializar lista para almacenar los factores primos
    factores_primos = []

    # Iterar desde 2 hasta la mitad del número
    for i in range(2, numero // 2 + 1):
        # Si el número es divisible por i, i es un factor primo
        while numero % i == 0:
            factores_primos.append(i)
            numero = numero // i

    # Si queda algún número mayor que 1, también es un factor primo
    if numero > 1:
        factores_primos.append(numero)

    # Imprimir los factores primos
    for factor in factores_primos:
        print(factor)

# Solicitar al usuario ingresar un número
numero = int(input())

# Llamar a la función para factorizar e imprimir los factores primos
factorizar_primos(numero)
