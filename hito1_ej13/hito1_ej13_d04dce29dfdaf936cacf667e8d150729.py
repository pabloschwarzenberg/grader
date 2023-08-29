#Factores Primos
def descomposicion_factores_primos(numero):
    # Inicializar la lista de factores primos
    factores_primos = []

    # Iterar desde 2 hasta la mitad del número (inclusive)
    for i in range(2, numero // 2 + 1):
        while numero % i == 0:
            factores_primos.append(i)
            numero //= i

    # Si el número es mayor que 1, es un factor primo
    if numero > 1:
        factores_primos.append(numero)

    # Imprimir cada factor primo en una línea separada
    for factor in factores_primos:
        print(factor)

# Pedir al usuario que ingrese un número
numero = int(input())

# Obtener la descomposición en factores primos e imprimirlos
descomposicion_factores_primos(numero)      