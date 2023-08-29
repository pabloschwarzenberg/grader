def jerigonzo(a):
    vocales=["a","e","i","o","u"]
    palabra1=""
    for letra in a:
        if letra in vocales:
            palabra1=palabra1+letra+"p"+letra  
        else:
            palabra1=palabra1+letra
    return palabra1