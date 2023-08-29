def traducir_a_jerigonzo(texto):
    jerigonzo = ""
    vocales = "aeiouAEIOU"
    for letra in texto:
        jerigonzo += letra
        if letra in vocales:
            jerigonzo += "p" + letra

    return jerigonzo

if __name__ == "__main__":
    # Solicitar el texto al usuario
    texto = input("Ingresa un texto: ")

    # Traducir el texto a jerigonzo
    texto_jerigonzo = traducir_a_jerigonzo(texto)

    # Imprimir el texto traducido
    print("Texto traducido a jerigonzo:", texto_jerigonzo)