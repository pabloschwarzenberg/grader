# por favor escribe aquí tu función
def es_primo(numero):
    cantidad = 0
    divisor = numero
    esPrimo = True
    if numero > 1:
        while divisor > 0:
            quociente = numero % divisor
            if quociente == 0:
                cantidad += 1
            if cantidad > 2:
                esPrimo = False
                break
            divisor -= 1
    else:
        esPrimo = False
    return esPrimo
           