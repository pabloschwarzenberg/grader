#Factores Primos
#Factores Primos
def descomposicion_factores_primos(numero):
    # Inicializamos la lista de factores primos
    factores_primos = []

    # Iteramos desde 2 hasta la mitad del número
    for i in range(2, numero // 2 + 1):
        # Mientras el número sea divisible por el factor, lo agregamos a la lista y dividimos el número
        while numero % i == 0:
            factores_primos.append(i)
            numero //= i

    # Si el número final es mayor a 1, también lo consideramos un factor primo
    if numero > 1:
        factores_primos.append(numero)

    # Imprimimos cada factor primo en una línea separada
    for factor in factores_primos:
        print(factor)

# Solicitamos al usuario que ingrese un número entero
numero = int(input())

# Llamamos a la función para obtener la descomposición en factores primos
descomposicion_factores_primos(numero)      