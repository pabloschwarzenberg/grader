def traducir_a_jerigonzo(texto):
    vocales = "aeiouáéíóú"
    texto_jerigonzo = ""
    for caracter in texto:
        if caracter.lower() in vocales:
            texto_jerigonzo += caracter + "p" + caracter.lower()
        else:
            texto_jerigonzo += caracter
    return texto_jerigonzo

if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print("Texto traducido a jerigonzo:")
    print(texto_traducido)
