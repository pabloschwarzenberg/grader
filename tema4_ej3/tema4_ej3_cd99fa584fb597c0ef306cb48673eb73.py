def traducir_jerigonzo(texto):
    vocales = "aeiouáéíóú"
    texto_traducido = ""
    for letra in texto:
        texto_traducido += letra
        if letra.lower() in vocales:
            texto_traducido += "p" + letra.lower()
    return texto_traducido

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = traducir_jerigonzo(texto)
    print("Texto traducido al jerigonzo:", texto_traducido)
