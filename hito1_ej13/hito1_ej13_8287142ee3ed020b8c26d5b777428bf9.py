#Factores Primos
def descomponer_factores_primos(numero):
    # Inicializamos una lista para almacenar los factores primos
    factores_primos = []

    # Dividimos el número entre 2 hasta que ya no sea divisible
    while numero % 2 == 0:
        factores_primos.append(2)
        numero = numero // 2

    # Dividimos el número entre los impares desde 3 hasta la raíz cuadrada del número
    # Incrementando de 2 en 2
    i = 3
    while i * i <= numero:
        while numero % i == 0:
            factores_primos.append(i)
            numero = numero // i
        i = i + 2

    # Si el número que queda después de la división es mayor a 2, es un factor primo
    if numero > 2:
        factores_primos.append(numero)

    # Imprimimos cada factor primo en una línea separada
    for factor in factores_primos:
        print(factor)

# Pedimos al usuario que ingrese un número
numero = int(input())

# Llamamos a la función para descomponer los factores primos e imprimirlos
descomponer_factores_primos(numero)
