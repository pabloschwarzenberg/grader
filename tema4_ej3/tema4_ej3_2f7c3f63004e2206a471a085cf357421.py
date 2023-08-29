def jerigonzo(string):
    vocales = ["a", "e", "i", "o", "u", "y"]
    letras = []
    pos = []
    for letra in string:
        letras.append(letra)
    i = 0
    while i < len(letras):
        if letras[i] in vocales:
            pos.append(i)
            i += 1
        else:
            i += 1
    for numero in pos:
        letras[numero] = letras[numero] + "p" + letras[numero]
    stringFinal = ""
    for l in letras:
        stringFinal += l
    string = stringFinal                                

    return string


