def jerigonzo(string):
    vocales = "aeiouAEIOU"
    nuevo_texto = ""
    for letra in string:
        if letra in vocales:
            nuevo_texto += letra + "p" + letra.lower()
        else:
            nuevo_texto += letra
    return nuevo_texto