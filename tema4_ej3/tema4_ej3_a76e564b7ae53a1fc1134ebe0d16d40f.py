def jerigonzo(texto):
    texto_traducido = ""
    for letra in texto:
        if letra.lower() in "aeiouáéíóú":
            texto_traducido += letra + "p" + letra.lower()
        else:
            texto_traducido += letra
    return texto_traducido

if __name__ == "__main__":
    texto = input("Ingresar un texto: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido:", texto_traducido)
