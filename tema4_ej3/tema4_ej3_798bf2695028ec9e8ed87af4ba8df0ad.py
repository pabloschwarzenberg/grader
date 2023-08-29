def traducir_a_jerigonzo(texto):
    jerigonzo = ""
    vocales = "aeiouáéíóú"
    for letra in texto:
        if letra.lower() in vocales:
            jerigonzo += letra + "p" + letra.lower()
        else:
            jerigonzo += letra
    return jerigonzo

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print("Texto traducido a jerigonzo:", texto_traducido)

