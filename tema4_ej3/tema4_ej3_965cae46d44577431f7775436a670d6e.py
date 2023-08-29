def jerigonzo(texto):
    vocales = "aeiou"
    texto_jerigonzo = ""
    for letra in texto:
        if letra.lower() in vocales:
            texto_jerigonzo += letra + "p" + letra.lower()
        else:
            texto_jerigonzo += letra
    return texto_jerigonzo

if __name__ == "_main_":
    texto = input("Ingrese un texto: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido a jerigonzo:", texto_traducido)