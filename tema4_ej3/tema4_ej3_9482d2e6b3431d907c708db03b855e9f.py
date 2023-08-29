def traducir_jerigonzo(texto):
    texto_jerigonzo = ""
    vocales = "aeiouáéíóú"
    for caracter in texto:
        if caracter.lower() in vocales:
            texto_jerigonzo += caracter + "p" + caracter.lower()
        else:
            texto_jerigonzo += caracter
    return texto_jerigonzo

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = traducir_jerigonzo(texto)
    print("Texto traducido al Jerigonzo:")
    print(texto_traducido)
