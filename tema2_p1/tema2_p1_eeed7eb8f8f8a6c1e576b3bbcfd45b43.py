# por favor escribe aquí tu función
def es_primo(numero):
    if numero == 1:
        return False
    elif numero == 2:
        return True
    else:
        for k in range (2, numero):
            if numero % k == 0:
                return False
        return True  