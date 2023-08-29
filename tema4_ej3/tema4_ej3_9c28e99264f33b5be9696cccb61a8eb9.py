def jerigonzo(palabra):
    vocales=["a","e","i","o","u"]
    palabra_jeri=""
    for letra in palabra:
        if letra in vocales:
            palabra_jeri += letra + "p" + letra
        else:
            palabra_jeri += letra
    return (palabra_jeri)

         