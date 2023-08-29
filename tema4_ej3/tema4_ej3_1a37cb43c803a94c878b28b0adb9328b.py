def traducir_a_jerigonzo(texto):
    texto_jerigonzo = ""
    vocales = "aeiouAEIOU"

    for letra in texto:
        if letra in vocales:
            texto_jerigonzo += letra + "p" + letra.lower()
        else:
            texto_jerigonzo += letra

    return texto_jerigonzo

if __name__ == "__main__":
    texto_original = input("Ingrese el texto a traducir: ")
    texto_traducido = traducir_a_jerigonzo(texto_original)
    print("Texto traducido:", texto_traducido)
