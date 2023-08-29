def jerigonzo(texto):
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    texto_jerigonzo = ""
    for letra in texto:
        if letra in vocales:
            texto_jerigonzo += letra + "p" + letra.lower()
        else:
            texto_jerigonzo += letra
    return texto_jerigonzo

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    print(jerigonzo(texto))
        