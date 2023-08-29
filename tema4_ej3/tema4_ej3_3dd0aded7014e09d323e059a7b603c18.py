def jerigonzo(string):
    vocales=["a","e","i","o","u"]
    jeri=""
    for letra in string:
        if letra in vocales:
            jeri=jeri+letra+"p"+letra
        else:
            jeri=jeri+letra
    return jeri
