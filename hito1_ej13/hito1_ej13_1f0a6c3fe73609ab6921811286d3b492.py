#Factores Primos
def factorizar_numero(numero):
    # Inicializar una lista vacía para almacenar los factores primos
    factores_primos = []

    # Iterar desde 2 hasta la mitad del número (inclusive)
    for i in range(2, numero // 2 + 1):
        # Verificar si el número es divisible por i
        while numero % i == 0:
            # Si es divisible, añadir i a la lista de factores primos
            factores_primos.append(i)
            # Dividir el número entre i
            numero = numero // i

    # Si después de la iteración el número es mayor que 1, añadirlo como factor primo
    if numero > 1:
        factores_primos.append(numero)

    # Imprimir cada factor primo en una línea separada
    for factor in factores_primos:
        print(factor)


# Solicitar al usuario que ingrese un número
numero = int(input())

# Llamar a la función para factorizar el número ingresado
factorizar_numero(numero)
