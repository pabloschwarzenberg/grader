# por favor escribe aquí tu función
def es_primo(numero):
    if(numero <= 1):
        return False
    if(numero <= 3):
        return True
    for i in range(2, int(numero/2)+1):
        if(numero%i == 0):
            return False
    return True
           