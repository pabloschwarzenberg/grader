def jerigonzo(texto):
    texto_jerigonzo = ""
    vocales = "aeiouáéíóú"
    
    for letra in texto:
        if letra.lower() in vocales:
            texto_jerigonzo += letra + "p" + letra.lower()
        else:
            texto_jerigonzo += letra

    return texto_jerigonzo

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido a jerigonzo:", texto_traducido)
