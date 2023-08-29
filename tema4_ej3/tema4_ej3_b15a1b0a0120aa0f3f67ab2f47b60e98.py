def jerigonzo(palabra):
    vocales=["a","e","i","o","u"]
    palabra_final=""
    for letra in palabra:
        if letra in vocales:
            palabra_final+=letra+"p"+letra
        else:
            palabra_final+=letra
    return (palabra_final)
         