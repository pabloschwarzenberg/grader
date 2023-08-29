# por favor escribe aquí tu función
def es_primo(numero):
    if numero == 1: 
        return False
    if numero % 2 == 0 and numero != 2: 
        return False
    return True
           