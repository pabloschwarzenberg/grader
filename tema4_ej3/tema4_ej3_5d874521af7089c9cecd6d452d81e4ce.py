def traducir_a_jerigonzo(texto):
    jerigonzo = ""
    for letra in texto:
        if letra in "aeiouAEIOUáéíóúÁÉÍÓÚ":
            jerigonzo += letra + "p" + letra
        else:
            jerigonzo += letra
    return jerigonzo

if __name__ == "__main__":
    texto_original = input("Ingresa un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto_original)
    print("Texto traducido: ", texto_traducido)
