def traducir_a_jerigonzo(texto):
    vocales = 'aeiouáéíóú'
    jerigonzo = ''
    for caracter in texto:
        if caracter.lower() in vocales:
            jerigonzo += caracter + 'p' + caracter.lower()
        else:
            jerigonzo += caracter
    return jerigonzo

texto = s
texto_traducido = traducir_a_jerigonzo(texto)
print('Texto traducido a jerigonzo:', texto_traducido)
