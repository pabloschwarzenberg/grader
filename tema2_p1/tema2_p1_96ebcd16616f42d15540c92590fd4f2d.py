# por favor escribe aquí tu función
def es_primo(numero):
    if (numero == 1) or (numero % 2 == 0):
        if (numero == 1) or (numero % 3 == 0):
            return False
        else:
            return True
    else:
        return True
    
