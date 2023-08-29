def jerigonzo(texto):
    vocales = "aeiouAEIOU"
    texto_jerigonzo = ""
    for caracter in texto:
        if caracter in vocales:
            texto_jerigonzo += caracter + "p" + caracter.lower()
        else:
            texto_jerigonzo += caracter
    return texto_jerigonzo

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_jerigonzo = jerigonzo(texto)
    print("Texto en jerigonzo:", texto_jerigonzo)
