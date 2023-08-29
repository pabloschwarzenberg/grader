def traducir_jerigonzo(texto):
    vocales = "aeiouAEIOU"
    texto_traducido = ""

    for letra in texto:
        if letra in vocales:
            texto_traducido += letra + "p" + letra.lower()
        else:
            texto_traducido += letra

    return texto_traducido

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = traducir_jerigonzo(texto)
    print("Texto traducido:", texto_traducido)
