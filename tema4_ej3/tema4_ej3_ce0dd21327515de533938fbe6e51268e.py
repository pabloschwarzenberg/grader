def traducir_jerigonzo(texto):
    resultado = ""
    vocales = "aeiouAEIOU"

    for letra in texto:
        resultado += letra
        if letra in vocales:
            resultado += "p" + letra.lower()
    return resultado
