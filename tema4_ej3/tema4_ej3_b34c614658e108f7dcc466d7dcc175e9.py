def jerigonzo(texto):
    texto_jerigonzo = ""
    vocales = "aeiouáéíóú"
    for caracter in texto:
        texto_jerigonzo += caracter
        if caracter.lower() in vocales:
            texto_jerigonzo += "p" + caracter.lower()
    return texto_jerigonzo
         