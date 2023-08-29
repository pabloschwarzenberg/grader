#Factores Primos
def factorizar(numero):
    # Inicializar una lista vacía para almacenar los factores primos
    factores_primos = []

    # Iterar desde 2 hasta el número dado
    for i in range(2, numero + 1):
        while numero % i == 0:  # Mientras el número sea divisible por i
            factores_primos.append(i)  # Agregar i a la lista de factores primos
            numero = numero / i  # Dividir el número por i

    # Imprimir los factores primos en líneas separadas
    for factor in factores_primos:
        print(factor)

# Pedir al usuario que ingrese un número
numero = int(input())

# Llamar a la función para factorizar el número ingresado
factorizar(numero)
     