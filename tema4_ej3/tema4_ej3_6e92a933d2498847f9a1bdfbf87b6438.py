def jerigonzo(string):
    letras = [i.lower() for i in string]
    for i in range(len(letras)):
        if letras[i] in ["a", "e", "i", "o", "u"]:
            letras[i] = (letras[i] + "p" + letras[i])
    return("".join(letras))