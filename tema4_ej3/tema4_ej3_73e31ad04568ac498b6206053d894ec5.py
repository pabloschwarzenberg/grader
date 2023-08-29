def jerigonzo(string):
    jerigonzo = ""
    vocales = "aeiouAEIOU"

    for letra in string:
        jerigonzo += letra
        if letra in vocales:
            jerigonzo += "p" + letra.lower()

    return jerigonzo

if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido a jerigonzo:", texto_traducido)
