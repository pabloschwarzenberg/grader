# por favor escribe aquí tu función
def es_primo(NUMERO):
    esPrimo= True
    if NUMERO == 1:
        esPrimo= False
    else:
        for x in range (2,NUMERO-1):
            if NUMERO % x == 0:
                esPrimo= False
                break
    return esPrimo
           