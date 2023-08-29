def traducir_jerigonzo(texto):
    vocales = "aeiouáéíóú"
    texto_traducido = ""
    for letra in texto:
        if letra.lower() in vocales:
            texto_traducido += letra + "p" + letra.lower()
        else:
            texto_traducido += letra
    return texto_traducido

    texto = input("Ingresa un texto: ")
    texto_traducido = traducir_(texto)
    print("Texto traducido:", texto_traducido)
