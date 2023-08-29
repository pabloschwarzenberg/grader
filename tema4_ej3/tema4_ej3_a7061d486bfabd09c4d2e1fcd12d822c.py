def traducir_jerigonzo(texto):
    jerigonzo = ""
    vocales = "aeiouAEIOU"

    for letra in texto:
        jerigonzo += letra
        if letra in vocales:
            jerigonzo += "p" + letra.lower()

    return jerigonzo

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = traducir_jerigonzo(texto)
    print("Texto traducido:", texto_traducido)
