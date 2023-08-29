def descomposicion_factores_primos(numero):
    factor = 2
    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero = numero / factor
        else:
            factor += 1
numero_ingresado = int(input())
descomposicion_factores_primos(numero_ingresado)

      