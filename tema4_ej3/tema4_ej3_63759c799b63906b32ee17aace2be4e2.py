def jerigonzo(palabra): 
    PALABRA = list(palabra)
    q = 0
    while q < len(PALABRA):

        if PALABRA[q] == "a":
            PALABRA[q] = PALABRA[q] + "p" + PALABRA[q]
        elif PALABRA[q] == "e":
            PALABRA[q] = PALABRA[q] + "p" + PALABRA[q]
        elif PALABRA[q] == "i":
            PALABRA[q] = PALABRA[q] + "p" + PALABRA[q]
        elif PALABRA[q] == "o":
            PALABRA[q] = PALABRA[q] + "p" + PALABRA[q]
        if PALABRA[q] == "u":
            PALABRA[q] = PALABRA[q] + "p" + PALABRA[q]
        else:
            PALABRA[q] = PALABRA[q]
        q = q + 1
    prueba = ''.join(PALABRA)
    return prueba