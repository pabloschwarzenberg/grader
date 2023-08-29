def traducir_a_jerigonzo(texto):
    vocales = "aeiouáéíóú"
    texto_traducido = ""
    for caracter in texto:
        if caracter.lower() in vocales:
            texto_traducido += caracter + "p" + caracter.lower()
        else:
            texto_traducido += caracter
    return texto_traducido

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print("Texto traducido a jerigonzo:", texto_traducido)
