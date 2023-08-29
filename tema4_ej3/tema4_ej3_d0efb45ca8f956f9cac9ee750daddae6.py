# Jerigonzo

def jerigonzo(string):
    palabra_traducida = ""
    vocales = "aeiou"
    for letra in string:
        if letra in vocales:
            palabra_traducida += letra
            palabra_traducida += "p"
        palabra_traducida += letra
    return palabra_traducida

    string = str(input("Ingrese palabra: "))
    print(jerigonzo(string))
    pass