def jerigonzo(texto):
    texto = texto.lower()
    vocales = 'aeiou'
    for vocal in vocales:
        texto = texto.replace(vocal, vocal+'p'+vocal)
    return texto

texto = "Hola, este es un texto de ejemplo"
print(jerigonzo(texto))