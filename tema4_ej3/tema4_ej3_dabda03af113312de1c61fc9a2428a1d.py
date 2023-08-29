def traducir_a_jerigonzo(texto):
    jerigonzo = ""
    for caracter in texto:
        if caracter.lower() in "aeiouáéíóú":
            jerigonzo += caracter + "p" + caracter.lower()
        else:
            jerigonzo += caracter
    return jerigonzo

if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print("Texto traducido al jerigonzo:", texto_traducido)
