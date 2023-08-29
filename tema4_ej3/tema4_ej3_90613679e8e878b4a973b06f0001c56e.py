def jerigonzo(string):
    vocales = "AEIOUaeiou"
    translate = ""
    for letra in string:
        if letra in vocales:
            translate += letra
            translate += "p"
        translate += letra
    return translate

