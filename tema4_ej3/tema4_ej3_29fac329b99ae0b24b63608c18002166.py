def jerigonzo(texto):
    texto = str(texto)
    texto_traducido = ""
    vocales = "aAeEiIoOuU"
    for i in range(len(texto)):
        if texto[i] in vocales:
            texto_traducido += texto[i] + "p" + texto[i]
        else:
            texto_traducido += texto[i]
    return texto_traducido