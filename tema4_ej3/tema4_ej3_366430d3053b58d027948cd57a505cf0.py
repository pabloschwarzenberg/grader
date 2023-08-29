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


if __name__ == "__main__":
    string = str(input("Ingrese palabra: "))
    print(jerigonzo(string))
    pass
         