# por favor escribe aquí tu función
def es_primo(numero):
    incremental = 1
    prueba = 0
    while numero >= incremental :
        if numero % incremental == 0 :
            prueba += 1
        incremental += 1
    if prueba == 2 :
        primo=True
    else :
        primo=False
    return primo