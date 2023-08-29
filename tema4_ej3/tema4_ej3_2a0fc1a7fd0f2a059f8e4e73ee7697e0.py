def jerigonzo(texto):
    vocales = "aeiouAEIOU"
    texto_jeri = ""
    for letra in texto:
        if letra in vocales:
            texto_jeri += letra + "p" + letra.lower()
        else:
            texto_jeri += letra
    return texto_jeri
