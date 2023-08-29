def jerigonzo(string):
    jerigonzo_texto = ""
    for letra in string:
        if letra.lower() in "aeiouáéíóú":
            jerigonzo_texto += letra + "p" + letra.lower()
        else:
            jerigonzo_texto += letra
    return jerigonzo_texto

if __name__ == "__main__":
    texto = input("Ingrese el texto a traducir: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido al jerigonzo:", texto_traducido)

         