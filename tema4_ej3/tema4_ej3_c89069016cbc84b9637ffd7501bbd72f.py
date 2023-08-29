def traducir_a_jerigonzo(texto):
    texto_traducido = ""
    vocales = "aeiouAEIOU"
    for caracter in texto:
        texto_traducido += caracter
        if caracter.lower() in vocales:
            texto_traducido += "p" + caracter.lower()
    return texto_traducido

