def jerigonzo(string):
    vocales="aeiou"
    jgonzo=""
    for letra in string:
        if letra in vocales:
            jgonzo=jgonzo+letra+"p"+letra
        else:
            jgonzo+=letra
    return jgonzo
    
