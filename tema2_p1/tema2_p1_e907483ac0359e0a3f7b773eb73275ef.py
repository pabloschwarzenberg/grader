def es_primo(Numero) :
    Primo=True
    if Numero == 1 :
        Primo=False
    else :
        for x in range(2, Numero-1):
            if Numero % x == 0:
                Primo=False
                break
    return Primo