def jerigonzo(string):
    jerigonzo_texto = ""
    for letra in string:
        if letra.lower() in "aeiouáéíóú":
            jerigonzo_texto += letra + "p" + letra.lower()
        else:
            jerigonzo_texto += letra
    return jerigonzo_texto

if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    texto_en_jerigonzo = jerigonzo(texto)
    print("Texto en jerigonzo:", texto_en_jerigonzo)
