def jerigonzo(texto):
    texto = texto.lower()
    vocales = 'aeiou'
    for vocal in vocales:
        texto = texto.replace(vocal, vocal+'p'+vocal)
    return texto         