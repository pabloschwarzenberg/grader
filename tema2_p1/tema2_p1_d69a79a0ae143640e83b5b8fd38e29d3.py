def es_primo(Numero):
    Es_Primo=True
    if Numero == 1:
        Es_Primo=False
    else:
        for x in range(2, Numero-1):
            if Numero % x == 0:
                Es_Primo=False
                break
    return Es_Primo