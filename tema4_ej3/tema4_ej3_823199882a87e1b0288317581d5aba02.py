def jerigonzo(texto):
    texto_traducido = ""
    vocales = "aeiouAEIOU"
    for caracter in texto:
        texto_traducido += caracter
        if caracter in vocales:
            texto_traducido += "p" + caracter.lower()
    return texto_traducido