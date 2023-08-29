# por favor escribe aquí tu función
def es_primo(numero):
    if numero <2:
        return False
    elif numero== 2:
        return True
    elif numero >2 and numero% 2 ==0:
        return False;
    else:
        for i in range(3, numero):
            if numero % i ==0:
                return False
    return True
           