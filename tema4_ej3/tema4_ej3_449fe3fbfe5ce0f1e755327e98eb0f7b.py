def jerigonzo(palabra):
    palabraJ = ''
    vocales = 'aeiou'
    for letra in palabra:
        if vocales.find(letra) != -1:
            if letra=='u' and palabra[palabra.index(letra)-1]=='q':
                palabraJ = palabraJ+letra
            else:
                palabraJ = palabraJ+letra+'p'+letra
        else:
            palabraJ = palabraJ+letra
    return palabraJ