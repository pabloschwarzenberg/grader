def jerigonzo(string):
    palabra_final = ""

    vocales = {"a", "e", "i", "o", "u"}

    for indice in string:
        if indice not in vocales:
            palabra_final += indice
        elif indice in vocales:
            palabra_final += indice+"p"+indice


    return palabra_final
