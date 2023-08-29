def jerigonzo(texto):
    vocales = "aeiouáéíóú"
    texto_jerigonzo = ""
    for letra in texto:
        if letra.lower() in vocales:
            texto_jerigonzo += letra + "p" + letra.lower()
        else:
            texto_jerigonzo += letra
    return texto_jerigonzo

if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print("Texto traducido a jerigonzo:", texto_traducido)
