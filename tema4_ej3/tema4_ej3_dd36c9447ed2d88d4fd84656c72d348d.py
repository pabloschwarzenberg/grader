def jerigonzo(string):
    vocales="aeoiuAEOIU"
    resultado=""
    for x in range(len(string)):
        if string[x] in vocales:
            resultado+=string[x]+"p"+string[x]
        else:
            resultado+=string[x]
    return resultado
