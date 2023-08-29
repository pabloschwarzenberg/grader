def jerigonzo(string):
    vocales = ["a", "e", "i", "o", "u"]
    string.lower()
    palabra = ""
    for letra in string:
        if (letra in vocales):
            palabra += letra
            palabra += "p"
            palabra += letra
        else:
            palabra += letra
    return palabra
         