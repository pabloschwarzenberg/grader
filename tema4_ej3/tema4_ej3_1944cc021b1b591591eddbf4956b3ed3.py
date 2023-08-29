def jerigonzo(texto):
    texto_jerigonzo = ""
    for letra in texto:
        if letra.lower() in "aeiouáéíóú":
            texto_jerigonzo += letra + "p" + letra.lower()
        else:
            texto_jerigonzo += letra
    return texto_jerigonzo

if __name__ == "__main__":
    texto_original = input("Ingrese el texto a traducir: ")
    texto_traducido = jerigonzo(texto_original)
    print("Texto traducido a jerigonzo:")
    print(texto_traducido)
