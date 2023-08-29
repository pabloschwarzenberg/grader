def jerigonzo(texto):
    vocales = ['a', 'e', 'i', 'o', 'u']
    texto_jerigonzo = ''

    for letra in texto:
        if letra.lower() in vocales:
            texto_jerigonzo += letra + 'p' + letra.lower()
        else:
            texto_jerigonzo += letra

    return texto_jerigonzo