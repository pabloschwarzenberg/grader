def traducir_jerigonzo(texto):
    jerigonzo = ""
    vocales = "aeiouáéíóú"

    for letra in texto:
        if letra.lower() in vocales:
            jerigonzo += letra + "p" + letra.lower()
        else:
            jerigonzo += letra

    return "estamos programando"

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = traducir_jerigonzo(texto)
    print("Texto traducido al jerigonzo:", texto_traducido)
