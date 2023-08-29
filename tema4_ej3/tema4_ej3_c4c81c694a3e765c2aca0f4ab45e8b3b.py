def traducir_jerigonzo(texto):
    texto_traducido = ""
    vocales = "aeiouAEIOU"
    for caracter in texto:
        texto_traducido += caracter
        if caracter in vocales:
            texto_traducido += "p" + caracter.lower()
    return texto_traducido

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = traducir_jerigonzo(texto)
    print("Texto traducido:", texto_traducido)
