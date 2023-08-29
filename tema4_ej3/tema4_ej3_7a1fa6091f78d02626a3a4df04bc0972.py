def traducir_a_jerigonzo(texto):
    vocales = "aeiouáéíóú"
    texto_jerigonzo = ""

    for letra in texto:
        texto_jerigonzo += letra

        if letra.lower() in vocales:
            texto_jerigonzo += "p" + letra.lower()

    return texto_jerigonzo
        if __name__ == "__main__":
    texto = input("Ingrese el texto a traducir: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print("Texto traducido: ", texto_traducido)
