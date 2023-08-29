def es_primo(Numero) :
    Es_=True
    if Numero == 1 :
        Es_=False
    else :
        for x in range(2, Numero-1):
            if Numero % x == 0:
                Es_=False
                break
    return Es_
           