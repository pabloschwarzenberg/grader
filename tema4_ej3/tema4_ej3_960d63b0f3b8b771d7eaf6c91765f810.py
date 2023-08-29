def traducir_a_jerigonzo(texto):
    texto_traducido = ""
    vocales = "aeiouAEIOU"

    for letra in texto:
        texto_traducido += letra
        if letra in vocales:
            texto_traducido += "p" + letra.lower()

    return texto_traducido
if __name__ == "__main__":
    texto_original = input("Ingresa un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto_original)
    print("Texto traducido: {}".format(texto_traducido))
