def jerigonzo(texto):
    jerigonzo_texto = ""
    for caracter in texto:
        if caracter.lower() in "aeiouáéíóú":
            jerigonzo_texto += caracter + "p" + caracter.lower()
        else:
            jerigonzo_texto += caracter
    return jerigonzo_texto

if __name__ == "__main__":
    texto = input("Ingrese el texto a traducir al Jerigonzo: ")
    texto_jerigonzo = jerigonzo(texto)
    print("Texto traducido al Jerigonzo:", texto_jerigonzo)
