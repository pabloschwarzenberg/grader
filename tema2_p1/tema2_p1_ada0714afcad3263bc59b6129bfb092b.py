# por favor escribe aquí tu función
def es_primo(NUMERO):
    if NUMERO<2:
        return False
    for num in range(2,NUMERO):
        if NUMERO % num == 0:
            return False
        return True
