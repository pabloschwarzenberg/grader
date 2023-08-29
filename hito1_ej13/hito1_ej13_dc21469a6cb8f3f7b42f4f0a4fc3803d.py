def descomponer_factores_primos(numero):
    # Comenzamos con el factor primo más pequeño: 2
    factor = 2
    while factor <= numero:
        if numero % factor == 0:
            # Si el número es divisible por el factor actual,
            # entonces el factor es primo
            print(factor)
            numero = numero / factor
        else:
            # Si no es divisible, probamos con el siguiente factor
            factor += 1
# Pedimos al usuario que ingrese el número
numero = int(input())
# Llamamos a la función para descomponer los factores primos
descomponer_factores_primos(numero)