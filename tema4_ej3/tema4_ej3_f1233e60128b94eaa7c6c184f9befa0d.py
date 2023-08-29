def traducir_a_jerigonzo(texto):
    jerigonzo = ""
    for letra in texto:
        if letra.lower() in "aeiouáéíóú":
            jerigonzo += letra + "p" + letra.lower()
        else:
            jerigonzo += letra
    return jerigonzo

if __name__ == "__main__":
    texto_original = input("Ingresa el texto a traducir: ")
    texto_traducido = traducir_a_jerigonzo(texto_original)
    print("Texto traducido a jerigonzo:", texto_traducido)
