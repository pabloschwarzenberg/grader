# por favor escribe aquí tu función
def es_primo(numero):
    if (numero == 1):
        return False
    elif (numero == 2):
        return True;
    else:
        for x in range(2,numero):
            if (numero % x==0):
                return False
        return True
           