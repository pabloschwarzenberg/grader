def traducir_a_jerigonzo(texto):
    texto_traducido = ""
    for letra in texto:
        if letra.lower() in "aeiou":
            texto_traducido += letra + "p" + letra.lower()
        else:
            texto_traducido += letra
    return texto_traducido
 