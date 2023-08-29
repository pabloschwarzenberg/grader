def descomposicion_factores_primos(numero):
    factor = 2

    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero = numero / factor
        else:
            factor += 1

# Ejemplo de uso
numero = int(input("Ingrese un número entero: "))
descomposicion_factores_primos(numero)
