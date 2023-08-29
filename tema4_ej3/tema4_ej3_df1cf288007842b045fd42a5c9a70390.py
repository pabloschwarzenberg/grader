def jerigonzo(string):
    vocales = 'aeiou'
    palabra = ''
    for letra in string:
        if letra.lower() in vocales:
            palabra += letra + 'p' + letra
        else:
            palabra += letra
        
    return palabra

         