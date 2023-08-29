def jerigonzo(string):
    vocales = 'aeiou'
    string = string.lower()
    palabra = ''
    for letra in string:
        palabra += letra
        if letra in vocales:
            palabra += 'p'+letra
        
    return palabra