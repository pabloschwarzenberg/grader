def traducir_jerigonzo(texto):
    texto_traducido = ""
    vocales = "aeiouAEIOU"
    for letra in texto:
        if letra in vocales:
            texto_traducido += letra + "p" + letra.lower()
        else:
            texto_traducido += letra
    return texto_traducido

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = traducir_jerigonzo(texto)
    print("Texto traducido: {}".format(texto_traducido))
