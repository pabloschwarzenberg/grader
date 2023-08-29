def jerigonzo(string):
    return string

if __name__ == "__main__":
    pass
def traducir_a_jerigonzo(texto):
    jerigonzo = ""
    vocales = "aeiouAEIOU"

    for letra in texto:
        if letra in vocales:
            jerigonzo += letra + "p" + letra.lower()
        else:
            jerigonzo += letra

    return jerigonzo

if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print("Texto traducido a jerigonzo:")
    print(texto_traducido)
