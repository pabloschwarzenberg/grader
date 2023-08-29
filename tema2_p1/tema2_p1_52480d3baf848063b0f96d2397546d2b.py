def es_primo(numero):
    if (numero % 2) == 0:
        n = False
    elif (numero % 2) != 0:
        if numero == 1:
            n = False
        else:
            n = True
    return n